from textual.app import ComposeResult
from textual.containers import Vertical
from textual.widgets import Input, Static
from textual import events

from controllers.terminal_controller import TerminalController

class TerminalView(Static):

    def __init__(self):
        super().__init__()

        self.controller = TerminalController()
        self.history = ""

        self.command_history = []
        self.history_index = 0

    def compose(self) -> ComposeResult:

        with Vertical():

            yield Static(
                "[bold cyan]SSH Terminal[/bold cyan]",
                id="terminal_title"
            )

            yield Static(
                "",
                id="terminal_output"
            )

            yield Input(
                placeholder="Type command...",
                id="terminal_input"
            )

    def on_input_submitted(self, event: Input.Submitted):

        command = event.value.strip()
        self.command_history.append(command)
        self.history_index = len(self.command_history)

        if not command:
            return

        if command == "clear":
            self.history = ""
            self.query_one(
                "#terminal_output",
                Static
            ).update("")
            event.input.value = ""
            return

        result = self.controller.execute(command)

        prompt = self.controller.prompt()
        self.history += f"{prompt} {command}\n"

        if result:
            self.history += result.rstrip()

        self.history += "\n\n"

        self.query_one(
            "#terminal_output",
            Static
        ).update(self.history)

        event.input.value = ""

    def on_key(self, event: events.Key):

        input_box = self.query_one("#terminal_input", Input)

        if event.key == "up":

            if self.command_history and self.history_index > 0:
                self.history_index -= 1
                input_box.value = self.command_history[self.history_index]

            event.prevent_default()

        elif event.key == "down":

            if self.history_index < len(self.command_history) - 1:
                self.history_index += 1
                input_box.value = self.command_history[self.history_index]
            else:
                self.history_index = len(self.command_history)
                input_box.value = ""

            event.prevent_default()

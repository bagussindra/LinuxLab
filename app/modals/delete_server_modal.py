from textual.app import ComposeResult
from textual.screen import ModalScreen
from textual.containers import Vertical
from textual.widgets import Label, Button

from services.server_service import ServerService


class DeleteServerModal(ModalScreen):

    CSS = """
    DeleteServerModal {
        align: center middle;
    }

    #dialog {
        width: 50;
        height: auto;

        border: round red;
        background: $surface;

        padding: 1 2;
    }

    Button {
        width: 100%;
        margin-top: 1;
    }
    """

    def __init__(self, server, index):
        super().__init__()

        self.server = server
        self.index = index

        self.server_service = ServerService()

    def compose(self) -> ComposeResult:

        with Vertical(id="dialog"):

            yield Label("[bold red]Delete Server[/bold red]")

            yield Label(
                f"Delete '{self.server['name']}' ?"
            )

            yield Button(
                "Yes",
                id="yes"
            )

            yield Button(
                "No",
                id="no"
            )

    def on_button_pressed(self, event: Button.Pressed):

        if event.button.id == "no":
            self.dismiss()

        elif event.button.id == "yes":

            self.server_service.delete(
                self.index
            )

            self.dismiss(True)

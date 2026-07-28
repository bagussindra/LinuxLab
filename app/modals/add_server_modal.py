from textual.app import ComposeResult
from textual.screen import ModalScreen
from textual.containers import Vertical
from textual.widgets import Input, Button, Label

from services.server_service import ServerService


class AddServerModal(ModalScreen):


    CSS = """
    AddServerModal {
        align: center middle;
    }

    #dialog {
        width: 60;
        height: auto;

        border: round cyan;

        background: $surface;

        padding: 1 2;
    }

    Input {
        margin-bottom: 1;
    }

    Button {
        width: 100%;
        margin-top: 1;
    }
    """

    def __init__(self):
        super().__init__()

        self.server_service = ServerService()

    def compose(self) -> ComposeResult:

        with Vertical(id="dialog"):

            yield Label("Add Server")

            yield Input(
                placeholder="Server Name",
                id="name"
            )

            yield Button(
                "Save",
                id="save"
            )

            yield Button(
                "Cancel",
                id="cancel"
            )

    def on_button_pressed(self, event: Button.Pressed):

        if event.button.id == "cancel":
            self.dismiss()
            return

        if event.button.id == "save":

            name = self.query_one("#name", Input).value.strip()

            if not name:
                self.notify("Server name is required.")
                return

            server = {
                "name": name,
                "host": "",
                "user": "",
                "password": "",
                "port": 22
            }

            self.server_service.add(server)

            self.dismiss(True)

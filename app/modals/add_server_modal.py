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

    def __init__(self, server=None, index=None):
        super().__init__()

        self.server_service = ServerService()

        self.server = server
        self.index = index

    def compose(self) -> ComposeResult:

        with Vertical(id="dialog"):

            yield Label("Add Server")

            yield Label("Name")
            yield Input(
                value=self.server["name"] if self.server else "",
                placeholder="Server Name",
                id="name"
            )

            yield Label("Host")
            yield Input(
                value=self.server["host"] if self.server else "",
                placeholder="103.179.xxx.xxx",
                id="host"
            )

            yield Label("Username")
            yield Input(
                value=self.server["user"] if self.server else "",
                placeholder="root",
                id="user"
            )

            yield Label("Password")
            yield Input(
                value=self.server["password"] if self.server else "",
                placeholder="Password",
                password=True,
                id="password"
            )

            yield Label("Port")
            yield Input(
                value=str(self.server["port"]) if self.server else "22",
                id="port"
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
            host = self.query_one("#host", Input).value.strip()
            user = self.query_one("#user", Input).value.strip()
            password = self.query_one("#password", Input).value
            port = self.query_one("#port", Input).value.strip()

            if not name or not host or not user:
                self.notify("Please fill all required fields.")
                return

            try:
                port = int(port)
            except ValueError:
                self.notify("Port must be a number.")
                return

            server = {
                "name": name,
                "host": host,
                "user": user,
                "password": password,
                "port": port,
            }

            if self.server is None:
                self.server_service.add(server)
            else:
                self.server_service.update(
                    self.index,
                    server
                )

            self.dismiss(True)


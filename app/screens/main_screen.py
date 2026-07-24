from textual.screen import Screen
from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Header, Footer, Static

from widgets.sidebar import Sidebar


class MainScreen(Screen):

    def compose(self) -> ComposeResult:

        yield Header(show_clock=True)

        with Horizontal():

            yield Sidebar()

            yield Static(
                "Welcome to LinuxLab",
                id="content"
            )

        yield Footer()

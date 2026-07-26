from textual.app import ComposeResult
from textual.widgets import Static

from controllers.network_controller import NetworkController
from widgets.ping_widget import PingWidget


class NetworkView(Static):

    def __init__(self):
        super().__init__()

        self.controller = NetworkController()

    def compose(self) -> ComposeResult:

        self.ping = PingWidget()

        yield self.ping

    def on_mount(self):

        self.refresh_ping()

    def refresh_ping(self):

        data = self.controller.ping("8.8.8.8")

        self.ping.update_ping(data)

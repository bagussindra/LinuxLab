from textual.app import ComposeResult
from textual.containers import Vertical
from textual.widgets import Static

from controllers.ssh_controller import SSHController

from widgets.system_widget import SystemWidget
from widgets.resource_widget import ResourceWidget
from widgets.network_widget import NetworkWidget

class DashboardView(Static):

    def __init__(self):
        super().__init__()

        self.controller = SSHController()

    def on_mount(self):

        self.refresh_dashboard()

    def on_show(self):

        self.refresh_dashboard()

    def refresh_dashboard(self):

        try:

            info = self.controller.system_info()

            self.system.update_info(info)
            self.resource.update_info(info)
            self.network.update_info(info)


        except Exception:

            self.update(
            """[bold cyan]Dashboard[/bold cyan]

[yellow]Not connected[/yellow]

Open SSH Manager
Press ENTER to connect.
"""
            )

    def compose(self) -> ComposeResult:

        with Vertical():

            self.system = SystemWidget()

            self.resource = ResourceWidget()

            self.network = NetworkWidget()

            yield self.system
            yield self.resource
            yield self.network

from textual.app import ComposeResult
from textual.widgets import Static
from textual.containers import Vertical, Horizontal

from controllers.ssh_controller import SSHController
from controllers.settings_controller import SettingsController

from widgets.system_widget import SystemWidget
from widgets.resource_widget import ResourceWidget
from widgets.network_widget import NetworkWidget

class DashboardView(Static):

    def __init__(self):
        super().__init__()

        self.settings = SettingsController()
        self.controller = SSHController()

    def on_mount(self):

        self.refresh_dashboard()
        self.start_refresh_timer()

    def on_show(self):

        self.refresh_dashboard()

    def start_refresh_timer(self):

        interval = self.settings.get("refresh_interval")

        if hasattr(self, "refresh_timer"):
            self.refresh_timer.stop()

        if interval > 0:
            self.refresh_timer = self.set_interval(
                interval,
                self.refresh_dashboard,
        )

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


            self.system = SystemWidget()

            self.resource = ResourceWidget()

            self.network = NetworkWidget()

            with Vertical():

                with Horizontal():

                    yield self.system
                    yield self.resource

                yield self.network

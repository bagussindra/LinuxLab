from textual.widgets import Static

from controllers.ssh_controller import SSHController

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

            self.update(
                f"""
[bold cyan]Dashboard[/bold cyan]

Hostname : {info["hostname"]}
OS       : {info["os"]}
Kernel   : {info["kernel"]}
CPU      : {info["cpu"]}
Memory   : {info["memory"]}
Disk     : {info["disk"]}
IP       : {info["ip"]}
Load     : {info["load"]}
Uptime   : {info["uptime"]}
"""
            )


        except Exception:

            self.update(
            """[bold cyan]Dashboard[/bold cyan]

[yellow]Not connected[/yellow]

Open SSH Manager
Press ENTER to connect.
"""
            )

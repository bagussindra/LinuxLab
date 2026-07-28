from textual.reactive import reactive
from textual.widgets import Static

from config.servers import SERVERS
from controllers.ssh_controller import SSHController
from controllers.settings_controller import SettingsController

class SSHView(Static):

    selected = reactive(0)

    def on_mount(self):
        self.render_servers()

    def render_servers(self):

        text = "[bold cyan]SSH Manager[/bold cyan]\n\n"

        text += "[bold]Servers[/bold]\n\n"

        for i, server in enumerate(SERVERS):

            if i == self.selected:
                text += f"▶ {server['name']}\n"
            else:
                text += f"  {server['name']}\n"

        text += "\nPress ENTER to connect."

        self.update(text)

    def cursor_up(self):

        self.selected = (self.selected - 1) % len(SERVERS)

        self.render_servers()

    def cursor_down(self):

        self.selected = (self.selected + 1) % len(SERVERS)

        self.render_servers()

    @property
    def current(self):
        return SERVERS[self.selected]

    def __init__(self):
        super().__init__()

        self.controller = SSHController()
        self.settings = SettingsController()

    def connect(self):

        server = self.current

        try:

            info = self.controller.connect(server)

            self.render_connected(info)

        except Exception as e:

            self.update(
                f"""
[bold red]Connection Failed[/bold red]

{e}
"""
            )

    def refresh_info(self):

        try:

            server = self.current

            info = self.controller.connect(server)

            self.render_connected(info)

        except Exception as e:

            self.update(
                f"""
[bold red]Connection Failed[/bold red]

{e}
"""
            )

    def disconnect(self):

        self.controller.disconnect()

        self.render_servers()

    def footer_text(self):

        interval = self.settings.get("refresh_interval")

        if interval == 0:
            return "[dim]Refresh : Manual (R)[/dim]"

        return f"[dim]Auto Refresh : {interval}s[/dim]"

    def render_connected(self, info):

        self.update(
            f"""
[bold cyan]SSH Manager[/bold cyan]

[bold green]● Connected[/bold green]

Hostname : {info["hostname"]}
OS       : {info["os"]}
Kernel   : {info["kernel"]}
CPU      : {info["cpu"]}
Memory   : {info["memory"]}
Disk     : {info["disk"]}
IP       : {info["ip"]}
Load     : {info["load"]}
Uptime   : {info["uptime"]}

{self.footer_text()}
"""
            )

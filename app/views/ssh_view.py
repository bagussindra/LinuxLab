from textual.reactive import reactive
from textual.widgets import Static

from config.servers import SERVERS
from controllers.ssh_controller import SSHController

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

    def connect(self):

        server = self.current

        try:

            info = self.controller.connect(server)

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
"""
            )
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

[dim]Press R to refresh[/dim]
"""
            )

        except Exception as e:

            self.update(
                f"""
[bold red]Refresh Failed[/bold red]

{e}
"""
            )

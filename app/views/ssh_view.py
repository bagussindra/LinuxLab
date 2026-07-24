import json
import socket

from textual.widgets import Static
from services.ssh_service import SSHService

class SSHView(Static):

    selected = 0

    def __init__(self):

        super().__init__()

        self.selected = 0

        self.ssh = SSHService()

    def on_mount(self):
        self.set_interval(2, self.refresh_servers)

    def check_port(self, host, port):
        try:
            sock = socket.create_connection((host, port), timeout=1)
            sock.close()
            return True
        except Exception:
            return False

    def refresh_servers(self):

        with open("config/servers.json") as f:
            servers = json.load(f)

        text = "🔐 SSH Manager\n\n"

        text += "Saved Servers\n"
        text += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"

        for index, server in enumerate(servers):

            status = (
                "🟢 Online"
                if self.check_port(server["host"], server["port"])
                else "🔴 Offline"
            )

            cursor = "▶" if index == self.selected else " "

            text += (
                f"{cursor} {server['name']}\n"
                f"   {server['user']}@{server['host']}\n"
                f"   Port   : {server['port']}\n"
                f"   Status : {status}\n\n"
            )

        text += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"

        text += "[A] Add Server\n"
        text += "[E] Edit Server\n"
        text += "[D] Delete Server\n"
        text += "[ENTER] Connect"

        self.update(text)

    def move_up(self):

        with open("config/servers.json") as f:
            servers = json.load(f)

        self.selected = (self.selected - 1) % len(servers)

        self.refresh_servers()

    def move_down(self):

        with open("config/servers.json") as f:
            servers = json.load(f)

        self.selected = (self.selected + 1) % len(servers)

        self.refresh_servers()

    def current_server(self):

        with open("config/servers.json") as f:
            servers = json.load(f)

        return servers[self.selected]


    def connect(self):

        server = self.current_server()

        try:

            self.ssh.connect(server)

            info = self.ssh.get_system_info()

            text = "🔐 SSH Manager\n\n"

            text += "🟢 Connected\n\n"

            text += f"Server   : {server['name']}\n"
            text += f"Host     : {server['host']}\n"
            text += f"User     : {server['user']}\n\n"

            text += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"

            text += f"Hostname : {info['hostname']}\n"
            text += f"Kernel   : {info['kernel']}\n"
            text += f"Uptime   : {info['uptime']}\n"
            text += f"Load Avg : {' '.join(info['load'])}\n\n"

            text += "Memory\n"
            text += info["memory"]
            text += "\n"

            text += "Disk\n"
            text += info["disk"]

            self.update(text)

        except Exception as e:

            self.update(
                f"❌ Connection Failed\n\n{e}"
            )

    def handle_key(self, event):

        if event.key == "up":

            self.move_up()

            return True

        elif event.key == "down":

            self.move_down()

            return True

        elif event.key == "enter":

            self.connect()

            return True

        return False

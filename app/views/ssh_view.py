import json
import socket
import subprocess

from textual.widgets import Static


class SSHView(Static):

    selected = 0

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

        subprocess.call([
            "ssh",
            "-p",
            str(server["port"]),
            f"{server['user']}@{server['host']}"
        ])

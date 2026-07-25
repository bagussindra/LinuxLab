import json

from textual.widgets import Static


class ServerListWidget(Static):

    def __init__(self):
        super().__init__()
        self.selected = 0
        self.servers = []

    def on_mount(self):

        with open("config/servers.json") as f:
            self.servers = json.load(f)

        self.refresh_list()

    def refresh_list(self):

        text = "[bold cyan]Servers[/bold cyan]\n\n"

        for i, server in enumerate(self.servers):

            cursor = "▶" if i == self.selected else " "

            text += (
                f"{cursor} {server['name']}\n"
            )

        self.update(text)

    def move_up(self):

        self.selected = (
            self.selected - 1
        ) % len(self.servers)

        self.refresh_list()

    def move_down(self):

        self.selected = (
            self.selected + 1
        ) % len(self.servers)

        self.refresh_list()

    def current(self):

        return self.servers[self.selected]

from textual.widgets import Static


class ServerListWidget(Static):

    def on_mount(self):
        self.update("Loading servers...")

from textual.widgets import Static


class ServerDetailWidget(Static):

    def on_mount(self):
        self.update("Select a server")

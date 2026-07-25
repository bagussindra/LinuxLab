from textual.widgets import Static


class NetworkView(Static):

    def on_mount(self):

        self.update(
            "[bold cyan]Network[/bold cyan]\n\n"
            "Network page"
        )

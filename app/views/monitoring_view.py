from textual.widgets import Static


class MonitoringView(Static):

    def on_mount(self):

        self.update(
            "[bold cyan]Monitoring[/bold cyan]\n\n"
            "Monitoring page"
        )

from textual.widgets import Static


class DashboardView(Static):

    def on_mount(self):

        self.update(
            "[bold cyan]Dashboard[/bold cyan]\n\n"
            "Welcome to LinuxLab 🚀"
        )

from textual.widgets import Static


class Content(Static):

    def show_dashboard(self):
        self.update(
            "[bold cyan]Dashboard[/bold cyan]\n\n"
            "Welcome to LinuxLab V2 🚀"
        )

    def show_monitoring(self):
        self.update(
            "[bold cyan]Monitoring[/bold cyan]\n\n"
            "Monitoring page"
        )

    def show_network(self):
        self.update(
            "[bold cyan]Network[/bold cyan]\n\n"
            "Network page"
        )

    def show_ssh(self):
        self.update(
            "[bold cyan]SSH Manager[/bold cyan]\n\n"
            "Press ENTER to connect."
        )

    def show_docker(self):
        self.update(
            "[bold cyan]Docker[/bold cyan]\n\n"
            "Docker page"
        )

    def show_settings(self):
        self.update(
            "[bold cyan]Settings[/bold cyan]\n\n"
            "Settings page"
        )

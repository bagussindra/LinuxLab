from textual.widgets import Static


class SSHStatusWidget(Static):

    def update_status(self, connected: bool):

        if connected:
            self.update(
                """
[bold cyan]SSH Status[/bold cyan]

[bold green]● Connected[/bold green]
"""
            )
        else:
            self.update(
                """
[bold cyan]SSH Status[/bold cyan]

[bold red]● Disconnected[/bold red]
"""
            )

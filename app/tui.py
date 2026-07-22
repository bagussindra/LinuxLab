from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Footer, Static


class Sidebar(Static):
    def compose(self) -> ComposeResult:
        yield Static(
"""[bold cyan]MENU[/bold cyan]

🏠 Dashboard
📊 Monitoring
🌐 Network
🔐 SSH Manager
🐳 Docker
⚙️ Settings
🚪 Exit
"""
        )


class Dashboard(Static):
    def compose(self) -> ComposeResult:
        yield Static(
"""[bold green]Welcome to LinuxLab[/bold green]

CPU   : ███████░░░░░ 45%

RAM   : █████░░░░░░░ 32%

DISK  : ████████░░░░ 61%

Status : Online
"""
        )


class LinuxLab(App):

    CSS = """
    Screen {
        layout: vertical;
    }

    Horizontal {
        height: 1fr;
    }

    Sidebar {
        width: 28;
        border: round cyan;
        padding: 1;
    }

    Dashboard {
        border: round green;
        padding: 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)

        with Horizontal():
            yield Sidebar()
            yield Dashboard()

        yield Footer()


if __name__ == "__main__":
    LinuxLab().run()

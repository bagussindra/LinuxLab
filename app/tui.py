from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Footer, Static
from textual.containers import Grid, Vertical
from textual import events

from widgets.cpu_widget import CPUWidget
from widgets.ram_widget import RAMWidget
from widgets.disk_widget import DiskWidget
from widgets.uptime_widget import UptimeWidget
from widgets.system_widget import SystemWidget
from widgets.network_widget import NetworkWidget

from views.dashboard_view import DashboardView
from views.monitoring_view import MonitoringView
from views.network_view import NetworkView
from views.ssh_view import SSHView
from views.docker_view import DockerView
from views.settings_view import SettingsView

class Sidebar(Static):

    def __init__(self):
        super().__init__()

        self.items = [
            "Dashboard",
            "Monitoring",
            "Network",
            "SSH Manager",
            "Docker",
            "Settings",
            "Exit"
        ]

    def on_mount(self):
        self.refresh_menu()

    def refresh_menu(self, selected=0):

        text = "[bold cyan]MENU[/bold cyan]\n\n"

        icons = [
            "🏠",
            "📊",
            "🌐",
            "🔐",
            "🐳",
            "⚙️",
            "🚪"
        ]

        for i, item in enumerate(self.items):

            line = f"{icons[i]} {item}"

            if i == selected:
                text += f"[reverse cyan]{line}[/reverse cyan]\n"
            else:
                text += line + "\n"

        self.update(text)

class Dashboard(Static):

    def __init__(self):
        super().__init__()

        self.views = {
            "Dashboard": DashboardView,
            "Monitoring": MonitoringView,
            "Network": NetworkView,
            "SSH Manager": SSHView,
            "Docker": DockerView,
            "Settings": SettingsView,
        }

    def show_view(self, name):

        self.remove_children()

        self.current_view = self.views[name]()

        self.mount(self.current_view)

class LinuxLab(App):

    MENU = [
        "Dashboard",
        "Monitoring",
        "Network",
        "SSH Manager",
        "Docker",
        "Settings",
        "Exit"
    ]

    selected = 0

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
        align: center top;
    }

    Dashboard {
        border: round green;
        padding: 1;
    }

    #dashboard-grid {
        grid-size: 2 2;
        grid-columns: 2fr 1.3fr;
        grid-rows: 7 7;
        grid-gutter: 1;
        height: 15;
    }

    SystemWidget {

        border: round yellow;
        margin-top: 1;
   	padding: 1;
	height: 8;
    }

    NetworkWidget {
    border: round magenta;
    padding: 1;
    margin-top: 1;
    height: 7;

    }

    CPUWidget,
    RAMWidget,
    DiskWidget,
    UptimeWidget {
        border: round cyan;
        padding: 1;
        height: 7;
    }
    ServerListWidget {
        width: 30;
        border: round cyan;
        padding: 1;
    }

    ServerDetailWidget {
        border: round green;
        padding: 1;
    }


    """

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)

        with Horizontal():
            self.sidebar = Sidebar()
            self.dashboard = Dashboard()
            yield self.sidebar
            yield self.dashboard

        yield Footer()

    def on_mount(self):

        self.dashboard.show_view("Dashboard")

    def on_key(self, event):
        print("KEY =", event.key)
        view = self.dashboard.current_view

        if hasattr(view, "handle_key"):
            if view.handle_key(event):
                return

        if event.key == "down":

            self.selected = (self.selected + 1) % len(self.MENU)

            self.sidebar.refresh_menu(self.selected)

            if self.MENU[self.selected] != "Exit":

                self.dashboard.show_view(
                    self.MENU[self.selected]
                )

        elif event.key == "up":

            self.selected = (self.selected - 1) % len(self.MENU)

            self.sidebar.refresh_menu(self.selected)

            if self.MENU[self.selected] != "Exit":

                self.dashboard.show_view(
                    self.MENU[self.selected]
                )

        elif event.key == "enter":

            if self.MENU[self.selected] == "Exit":
                self.exit()

        elif self.MENU[self.selected] == "SSH Manager":
            self.dashboard.current_view.connect()

if __name__ == "__main__":
    LinuxLab().run()

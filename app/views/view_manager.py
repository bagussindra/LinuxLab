from textual.containers import Container

from views.dashboard_view import DashboardView
from views.monitoring_view import MonitoringView
from views.network_view import NetworkView
from views.ssh_view import SSHView
from views.docker_view import DockerView
from views.settings_view import SettingsView


class ViewManager(Container):

    VIEWS = {
        "Dashboard": DashboardView,
        "Monitoring": MonitoringView,
        "Network": NetworkView,
        "SSH Manager": SSHView,
        "Docker": DockerView,
        "Settings": SettingsView,
    }

    def show(self, name: str):

        self.remove_children()

        view = self.VIEWS[name]()

        self.mount(view)

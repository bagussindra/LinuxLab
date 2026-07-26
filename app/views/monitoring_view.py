from textual.app import ComposeResult
from textual.widgets import Static

from controllers.monitor_controller import MonitorController
from widgets.monitor_widget import MonitorWidget


class MonitoringView(Static):

    def __init__(self):

        super().__init__()

        self.controller = MonitorController()

    def compose(self) -> ComposeResult:

        self.monitor = MonitorWidget()

        yield self.monitor

    def on_mount(self):

        self.refresh_status()

    def refresh_status(self):

        self.monitor.update_status(
            self.controller.status()
        )

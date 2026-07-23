from textual.app import ComposeResult
from textual.containers import Grid, Vertical
from textual.widgets import Static

from widgets.cpu_widget import CPUWidget
from widgets.ram_widget import RAMWidget
from widgets.disk_widget import DiskWidget
from widgets.uptime_widget import UptimeWidget
from widgets.network_widget import NetworkWidget
from widgets.system_widget import SystemWidget


class DashboardView(Static):

    def compose(self) -> ComposeResult:

        with Vertical():

            with Grid(id="dashboard-grid"):

                yield CPUWidget()
                yield RAMWidget()
                yield DiskWidget()
                yield UptimeWidget()

            yield NetworkWidget()

            yield SystemWidget()

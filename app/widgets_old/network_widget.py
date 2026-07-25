from textual.widgets import Static
import psutil


class NetworkWidget(Static):

    def on_mount(self):
        self.last = psutil.net_io_counters()
        self.set_interval(1, self.refresh_network)

    def refresh_network(self):
        current = psutil.net_io_counters()

        upload = (current.bytes_sent - self.last.bytes_sent) / 1024
        download = (current.bytes_recv - self.last.bytes_recv) / 1024

        self.last = current

        self.update(
            f"""🌐 Network

⬆ Upload   : {upload:.1f} KB/s

⬇ Download : {download:.1f} KB/s
"""
        )

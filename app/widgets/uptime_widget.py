from textual.widgets import Static
import psutil
import time


class UptimeWidget(Static):

    def on_mount(self):
        self.set_interval(1, self.refresh_uptime)

    def refresh_uptime(self):
        uptime = time.time() - psutil.boot_time()

        days = int(uptime // 86400)
        hours = int((uptime % 86400) // 3600)
        mins = int((uptime % 3600) // 60)

        self.update(
f"""🕒 Uptime

{days}d {hours}h {mins}m
"""
        )

from widgets.metric_card import MetricCard
import psutil


class DiskWidget(MetricCard):

    def on_mount(self):
        self.set_interval(2, self.refresh_disk)

    def refresh_disk(self):
        disk = psutil.disk_usage("/").percent

        self.set_metric(
            "Disk Usage",
            f"{disk:.1f} %",
            disk,
            "💾"
        )

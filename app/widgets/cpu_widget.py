from widgets.metric_card import MetricCard
import psutil


class CPUWidget(MetricCard):

    def on_mount(self):
        self.set_interval(1, self.refresh_cpu)

    def refresh_cpu(self):
        cpu = psutil.cpu_percent()

        self.set_metric(
            "CPU Usage",
            f"{cpu:.1f} %",
            cpu,
            "🖥"
        )

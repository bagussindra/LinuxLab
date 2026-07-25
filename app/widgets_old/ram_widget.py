from widgets.metric_card import MetricCard
import psutil


class RAMWidget(MetricCard):

    def on_mount(self):
        self.set_interval(1, self.refresh_ram)

    def refresh_ram(self):
        ram = psutil.virtual_memory().percent

        self.set_metric(
            "RAM Usage",
            f"{ram:.1f} %",
            ram,
            "🧠"
        )

from textual.widgets import Static


class MetricCard(Static):

    def set_metric(self, title, value, percent, icon="⚡"):

        total = 20
        filled = int(percent / 100 * total)

        bar = "█" * filled + "░" * (total - filled)

        self.update(
            f"{icon} {title}\n\n"
            f"{bar}\n\n"
            f"{value}"
        )

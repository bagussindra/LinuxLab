from textual.widgets import Static


class MonitorWidget(Static):

    def icon(self, ok):
        return "🟢" if ok else "🔴"

    def update_status(self, data):

        self.update(
            f"""
[bold cyan]📊 Monitoring[/bold cyan]

{self.icon(data["ssh"])} SSH Connection

{self.icon(data["cpu"])} CPU Usage       {data["cpu_usage"]}%

{self.icon(data["memory"])} Memory Usage    {data["memory_usage"]}%

{self.icon(data["disk"])} Disk Usage       {data["disk_usage"]}%

{self.icon(data["internet"])} Internet

{self.icon(data["docker"])} Docker

{self.icon(data["nginx"])} Nginx
"""
    )

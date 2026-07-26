from textual.widgets import Static


class PingWidget(Static):

    def update_ping(self, data):

        icon = "🟢" if data["reachable"] else "🔴"

        self.update(
            f"""
[bold cyan]🌐 Ping[/bold cyan]

Host      : {data["host"]}

Packets   : {data["received"]}/{data["sent"]}

Loss      : {data["loss"]}%

Average   : {data["avg"]} ms

Status    : {icon} Reachable
"""
        )

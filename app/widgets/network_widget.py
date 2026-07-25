from textual.widgets import Static


class NetworkWidget(Static):

    def update_info(self, info):

        self.update(
            f"""
[bold cyan]🌐 Network[/bold cyan]

IP     : {info["ip"]}
Load   : {info["load"]}
Uptime : {info["uptime"]}
"""
        )

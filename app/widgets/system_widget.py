from textual.widgets import Static


class SystemWidget(Static):

    def update_info(self, info):

        self.update(
            f"""
[bold cyan]🖥 System[/bold cyan]

Hostname : {info["hostname"]}
OS       : {info["os"]}
Kernel   : {info["kernel"]}
"""
        )

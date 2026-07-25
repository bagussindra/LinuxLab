from textual.widgets import Static


class ResourceWidget(Static):

    def update_info(self, info):

        self.update(
            f"""
[bold cyan]💻 Resource[/bold cyan]

CPU    : {info["cpu"]}
Memory : {info["memory"]}
Disk   : {info["disk"]}
"""
        )

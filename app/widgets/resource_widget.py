from textual.widgets import Static


class ResourceWidget(Static):

    def bar(self, percent: int):

        total = 20

        filled = int(total * percent / 100)

        return "█" * filled + "░" * (total - filled)

    def update_info(self, info):

        cpu = int(info["cpu_usage"])
        mem = int(info["memory_usage"])
        disk = int(info["disk_usage"])

        self.update(
            f"""
[bold cyan]💻 Resource[/bold cyan]

CPU

{self.bar(cpu)} {cpu}%

{info["cpu"]}

Memory

{self.bar(mem)} {mem}%

{info["memory"]}

Disk

{self.bar(disk)} {disk}%

{info["disk"]}
"""
        )

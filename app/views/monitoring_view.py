import os
import psutil

from textual.widgets import Static


class MonitoringView(Static):

    def on_mount(self):
        self.set_interval(1, self.refresh_process)

    def progress_bar(self, percent):

        total = 20
        filled = int(percent / 100 * total)

        bar = "█" * filled + "░" * (total - filled)

        if percent >= 80:
            color = "red"
        elif percent >= 50:
            color = "yellow"
        else:
            color = "green"

        return f"[{color}]{bar}[/{color}] {percent:.1f}%"

    def refresh_process(self):

        processes = []

        for proc in psutil.process_iter(
            ["pid", "name", "cpu_percent", "memory_info"]
        ):
            try:
                processes.append(proc.info)
            except Exception:
                pass

        processes.sort(
            key=lambda p: p["cpu_percent"],
            reverse=True,
        )

        cpu_usage = psutil.cpu_percent()

        ram = psutil.virtual_memory()

        swap = psutil.swap_memory()

        load = os.getloadavg()

        text = "📊 Monitoring\n\n"

        text += f"CPU Core   : {psutil.cpu_count()}\n"
        text += f"Processes  : {len(processes)}\n"
        text += f"Load Avg   : {load[0]:.2f}  {load[1]:.2f}  {load[2]:.2f}\n\n"

        text += "CPU Usage\n"
        text += self.progress_bar(cpu_usage) + "\n\n"

        text += "RAM Usage\n"
        text += self.progress_bar(ram.percent) + "\n\n"

        text += "Swap Usage\n"
        text += self.progress_bar(swap.percent) + "\n\n"

        text += (
            "PID".ljust(8)
            + "NAME".ljust(24)
            + "CPU".rjust(8)
            + "RAM".rjust(12)
            + "\n"
        )

        text += "-" * 60 + "\n"

        for p in processes[:15]:

            cpu = p["cpu_percent"]

            mem = p["memory_info"].rss / 1024 / 1024

            if cpu >= 70:
                cpu_text = f"[red]{cpu:>6.1f}%[/red]"
            elif cpu >= 30:
                cpu_text = f"[yellow]{cpu:>6.1f}%[/yellow]"
            else:
                cpu_text = f"[green]{cpu:>6.1f}%[/green]"

            text += (
                str(p["pid"]).ljust(8)
                + str(p["name"])[:22].ljust(24)
                + cpu_text
                + f"{mem:>9.1f} MB\n"
            )

        self.update(text)

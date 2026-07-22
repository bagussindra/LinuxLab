import socket
import platform
import psutil

from rich.table import Table


def system_table():

    table = Table(title="System Information")

    table.add_column("Item", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Hostname", socket.gethostname())
    table.add_row("OS", platform.system())
    table.add_row("Kernel", platform.release())
    table.add_row("Python", platform.python_version())
    table.add_row("CPU Cores", str(psutil.cpu_count()))
    table.add_row("Memory", f"{round(psutil.virtual_memory().total/1024**3,2)} GB")

    return table

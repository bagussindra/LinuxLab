from pyfiglet import figlet_format
from rich.console import Console
import platform
import socket
import psutil

console = Console()

console.print(
    figlet_format("LinuxLab", font="slant"),
    style="cyan"
)

console.print("[bold green]Learning Linux • Python • DevOps[/bold green]\n")

console.print(f"[cyan]Hostname :[/cyan] {socket.gethostname()}")
console.print(f"[cyan]OS       :[/cyan] {platform.system()} {platform.release()}")
console.print(f"[cyan]Python   :[/cyan] {platform.python_version()}")
console.print(f"[cyan]CPU Core :[/cyan] {psutil.cpu_count()}")
console.print(f"[cyan]Memory   :[/cyan] {round(psutil.virtual_memory().total/1024**3,1)} GB")

print()

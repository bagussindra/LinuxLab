from rich.console import Console
from rich.panel import Panel
import pyfiglet

console = Console()


def show_header():
    logo = pyfiglet.figlet_format("LinuxLab", font="slant")

    console.print(
        Panel.fit(
            f"[bold cyan]{logo}[/bold cyan]",
            title="[bold green]LinuxLab[/bold green]",
            subtitle="Learning Linux • Python • DevOps",
        )
    )

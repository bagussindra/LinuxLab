from rich.console import Console

console = Console()


def show_dashboard():

    console.print("\n[bold yellow]Menu[/bold yellow]\n")

    console.print("[1] Dashboard")
    console.print("[2] Monitoring")
    console.print("[3] Network")
    console.print("[4] Exit")

from rich.console import Console

from ui.header import show_header
from core.system import system_table
from modules.dashboard import show_dashboard

console = Console()


def main():

    console.clear()

    show_header()

    console.print(system_table())

    show_dashboard()

    choice = console.input("\n[bold cyan]linuxlab > [/bold cyan]")

    console.print(f"\nKamu memilih: [green]{choice}[/green]")


if __name__ == "__main__":
    main()

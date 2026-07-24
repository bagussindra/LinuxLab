from textual.widgets import Static


class Sidebar(Static):

    ITEMS = [
        "Dashboard",
        "Monitoring",
        "Network",
        "SSH Manager",
        "Docker",
        "Settings",
        "Exit",
    ]

    ICONS = [
        "🏠",
        "📊",
        "🌐",
        "🔐",
        "🐳",
        "⚙️",
        "🚪",
    ]

    def __init__(self):
        super().__init__()
        self.selected = 0

    def on_mount(self):
        self.refresh()

    def move_up(self):
        self.selected = (self.selected - 1) % len(self.ITEMS)
        self.refresh()

    def move_down(self):
        self.selected = (self.selected + 1) % len(self.ITEMS)
        self.refresh()

    @property
    def current(self):
        return self.ITEMS[self.selected]

    def refresh(self):

        text = "[bold cyan]MENU[/bold cyan]\n\n"

        for i, item in enumerate(self.ITEMS):

            line = f"{self.ICONS[i]} {item}"

            if i == self.selected:
                text += f"[reverse cyan]{line}[/reverse cyan]\n"
            else:
                text += line + "\n"

        self.update(text)

from textual.reactive import reactive
from textual.widgets import Static


class Sidebar(Static):

    ITEMS = [
        "Dashboard",
        "Monitoring",
        "Network",
        "SSH Manager",
        "Terminal",
        "Docker",
        "Settings",
        "Exit",
    ]

    ICONS = [
        "🏠",
        "📊",
        "🌐",
        "🔐",
        "💻",
        "🐳",
        "⚙️",
        "🚪",
    ]

    selected = reactive(0)

    def on_mount(self):
        self.render_menu()

    def render_menu(self):

        text = "[bold cyan]MENU[/bold cyan]\n\n"

        for i, item in enumerate(self.ITEMS):

            line = f"{self.ICONS[i]} {item}"

            if i == self.selected:
                text += f"[reverse]{line}[/reverse]\n"
            else:
                text += line + "\n"

        self.update(text)

    def cursor_up(self):
        self.selected = (self.selected - 1) % len(self.ITEMS)
        self.render_menu()

    def cursor_down(self):
        self.selected = (self.selected + 1) % len(self.ITEMS)
        self.render_menu()

    @property
    def current(self):
        return self.ITEMS[self.selected]

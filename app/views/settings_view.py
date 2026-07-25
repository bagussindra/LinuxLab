from textual.reactive import reactive
from textual.widgets import Static

from controllers.settings_controller import SettingsController


class SettingsView(Static):

    selected = reactive(0)
    option_selected = reactive(0)
    mode = reactive("menu")

    ITEMS = [
        "Theme",
        "Auto Refresh",
        "SSH Timeout",
    ]

    REFRESH_OPTIONS = [0, 3, 5, 10, 30, 60]

    @property
    def current(self):
        return self.ITEMS[self.selected]

    def __init__(self):
        super().__init__()

        self.settings = SettingsController()

    def on_mount(self):
        self.refresh_view()

    def refresh_view(self):

        if self.mode == "menu":
            self.render_menu()

        elif self.mode == "refresh":
            self.render_refresh()

    def render_menu(self):

        refresh = self.settings.get("refresh_interval")

        if refresh == 0:
            refresh = "OFF"
        else:
            refresh = f"{refresh} sec"

        text = f"""[bold cyan]Settings[/bold cyan]

{"▶" if self.selected == 0 else " "} Theme          : {self.settings.get("theme")}
{"▶" if self.selected == 1 else " "} Auto Refresh   : {refresh}
{"▶" if self.selected == 2 else " "} SSH Timeout    : {self.settings.get("ssh_timeout")} sec
"""

        self.update(text)

    def render_refresh(self):

        text = "[bold cyan]Auto Refresh[/bold cyan]\n\n"

        for i, option in enumerate(self.REFRESH_OPTIONS):

            if option == 0:
                label = "OFF"
            else:
                label = f"{option} sec"

            if i == self.option_selected:
                text += f"▶ {label}\n"
            else:
                text += f"  {label}\n"

        self.update(text)

    def open(self):

        if self.current == "Auto Refresh":

            self.mode = "refresh"

            self.refresh_view()

    def select_option(self):

        if self.mode != "refresh":
            return

        value = self.REFRESH_OPTIONS[self.option_selected]

        self.settings.set("refresh_interval", value)

        self.mode = "menu"

        self.refresh_view()

    def cursor_up(self):

        if self.mode == "menu":

            self.selected = (self.selected - 1) % len(self.ITEMS)

        elif self.mode == "refresh":

            self.option_selected = (
                self.option_selected - 1
            ) % len(self.REFRESH_OPTIONS)


        self.refresh_view()

    def cursor_down(self):

        if self.mode == "menu":

            self.selected = (self.selected + 1) % len(self.ITEMS)

        elif self.mode == "refresh":

            self.option_selected = (
                self.option_selected + 1
            ) % len(self.REFRESH_OPTIONS)

        self.refresh_view()

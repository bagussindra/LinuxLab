from textual.app import App

from screens.main_screen import MainScreen


class LinuxLab(App):

    TITLE = "LinuxLab"
    SUB_TITLE = "Cloud Engineer Toolkit"

    CSS_PATH = "style.tcss"

    def on_mount(self):

        self.push_screen(MainScreen())

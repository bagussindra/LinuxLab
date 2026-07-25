from textual.app import App

from screens.main_screen import MainScreen


class LinuxLab(App):

    def on_mount(self) -> None:
        self.push_screen(MainScreen())


if __name__ == "__main__":
    LinuxLab().run()

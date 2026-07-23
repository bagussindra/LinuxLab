from textual.widgets import Static


class SettingsView(Static):

    def on_mount(self):

        self.update(
"""⚙ Settings

Coming Soon...

- Theme
- Config
- About
"""
        )

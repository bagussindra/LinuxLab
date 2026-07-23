from textual.widgets import Static


class DockerView(Static):

    def on_mount(self):

        self.update(
"""🐳 Docker

Coming Soon...

- Container
- Image
- Volume
"""
        )

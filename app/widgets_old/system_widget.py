from textual.widgets import Static
import platform
import socket


class SystemWidget(Static):

    def on_mount(self):
        self.refresh_info()

    def refresh_info(self):
        self.update(
f"""🖥 System Information

Hostname : {socket.gethostname()}

OS       : {platform.system()}

Kernel   : {platform.release()}

Python   : {platform.python_version()}
"""
        )

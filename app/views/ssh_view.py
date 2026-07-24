from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Static

from widgets.server_list_widget import ServerListWidget
from widgets.server_detail_widget import ServerDetailWidget
from services.ssh_service import SSHService

class SSHView(Static):

    def __init__(self):
        super().__init__()

        self.service = SSHService()

    def compose(self) -> ComposeResult:

        self.server_list = ServerListWidget()
        self.server_detail = ServerDetailWidget()

        with Horizontal():

            yield self.server_list

            yield self.server_detail

    def on_mount(self):

        server = self.server_list.current()

        self.server_detail.update(
            f"Selected : {server['name']}\n\nPress ENTER to connect."
        )

    def move_up(self):

        self.server_list.move_up()

        server = self.server_list.current()

        self.server_detail.update(
            f"Selected : {server['name']}\n\nPress ENTER to connect."
        )

    def move_down(self):

        self.server_list.move_down()

        server = self.server_list.current()

        self.server_detail.update(
            f"Selected : {server['name']}\n\nPress ENTER to connect."
        )

    def connect(self):

        server = self.server_list.current()

        self.service.connect(server)

        info = self.service.get_system_info()

        self.server_detail.show_info(info)

    def handle_key(self, event):

        if event.key == "up":

            self.move_up()
            return True

        elif event.key == "down":

            self.move_down()
            return True

        elif event.key == "enter":

            self.connect()
            return True

        return False

from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Static

from widgets.server_list_widget import ServerListWidget
from widgets.server_detail_widget import ServerDetailWidget


class SSHView(Static):

    def compose(self) -> ComposeResult:

        self.server_list = ServerListWidget()
        self.server_detail = ServerDetailWidget()

        with Horizontal():

            yield self.server_list

            yield self.server_detail

    def on_mount(self):

        self.server_detail.show_server(
            self.server_list.current()
        )

    def move_up(self):

        self.server_list.move_up()

        self.server_detail.show_server(
            self.server_list.current()
        )

    def move_down(self):

        self.server_list.move_down()

        self.server_detail.show_server(
            self.server_list.current()
        )

    def handle_key(self, event):

        if event.key == "up":

            self.move_up()
            return True

        elif event.key == "down":

            self.move_down()
            return True

        return False

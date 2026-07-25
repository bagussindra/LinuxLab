from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.screen import Screen
from textual.widgets import Header, Footer, Static
from textual.binding import Binding
from views.view_manager import ViewManager


from widgets.sidebar import Sidebar


class MainScreen(Screen):

    CSS = """
    Horizontal {
        height: 1fr;
    }

    #sidebar {
        width: 30;
        border: round cyan;
        padding: 1;
    }

    #content {
        border: round green;
        padding: 1;
    }
    """

    BINDINGS = [
        Binding("up", "up", "Up"),
        Binding("down", "down", "Down"),
        Binding("left", "left", "Back"),
        Binding("right", "right", "Open"),
        Binding("enter", "select", "Select"),
        Binding("r", "refresh", "Refresh"),
    ]

    focus = "sidebar"

    def compose(self) -> ComposeResult:

        yield Header(show_clock=True)

        with Horizontal():

            yield Sidebar(id="sidebar")

            self.view = ViewManager(id="content")

            yield self.view


        yield Footer()

    def action_up(self):

        if self.focus == "sidebar":

            sidebar = self.query_one(Sidebar)

            sidebar.cursor_up()

            self.refresh_content()

        elif self.focus == "ssh":

            from views.ssh_view import SSHView

            ssh = self.view.query_one(SSHView)

            ssh.cursor_up()

    def action_down(self):

        if self.focus == "sidebar":

            sidebar = self.query_one(Sidebar)

            sidebar.cursor_down()

            self.refresh_content()

        elif self.focus == "ssh":

            from views.ssh_view import SSHView

            ssh = self.view.query_one(SSHView)

            ssh.cursor_down()

    def action_select(self):

        if self.focus == "sidebar":

            menu = self.query_one(Sidebar).current

            if menu == "Exit":
                self.app.exit()

            return

        elif self.focus == "ssh":

            from views.ssh_view import SSHView

            ssh = self.view.query_one(SSHView)

            ssh.connect()

    def action_refresh(self):

        if self.focus != "ssh":
            return

        from views.ssh_view import SSHView

        ssh = self.view.query_one(SSHView)

        ssh.refresh_info()

    def refresh_content(self):

        menu = self.query_one(Sidebar).current

        if menu != "Exit":
            self.view.show(menu)

    def on_mount(self):

        self.view = self.query_one(ViewManager)

        self.refresh_content()

    def action_right(self):

        menu = self.query_one(Sidebar).current

        if menu == "SSH Manager":

            self.focus = "ssh"

            from views.ssh_view import SSHView

            ssh = self.view.query_one(SSHView)

            ssh.focus()
            print("Focus -> SSH")

    def action_left(self):

        self.focus = "sidebar"

        sidebar = self.query_one(Sidebar)

        sidebar.focus()
        print("Focus -> Sidebar")

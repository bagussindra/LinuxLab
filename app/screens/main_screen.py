from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.screen import Screen
from textual.widgets import Header, Footer, Static
from textual.binding import Binding
from views.view_manager import ViewManager

from modals.add_server_modal import AddServerModal


from widgets.sidebar import Sidebar


class MainScreen(Screen):

    CSS = """
    Horizontal {
        height: auto;
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

    SystemWidget,
    ResourceWidget,
    PingWidget,
    InterfaceWidget {
         width: 1fr;

    }

    NetworkWidget {
        width: 100%;
    }

    SystemWidget,
    ResourceWidget,
    NetworkWidget,
    PingWidget,
    InterfaceWidget {
        border: round cyan;
        margin-bottom: 1;
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
        Binding("escape", "disconnect", "Disconnect"),
        Binding("a", "add_server", "Add"),
        Binding("e", "edit_server", "Edit"),
        Binding("d", "delete_server", "Delete"),

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

        elif self.focus == "settings":

            from views.settings_view import SettingsView

            settings = self.view.query_one(SettingsView)

            settings.cursor_up()

    def action_down(self):

        if self.focus == "sidebar":

            sidebar = self.query_one(Sidebar)

            sidebar.cursor_down()

            self.refresh_content()

        elif self.focus == "ssh":

            from views.ssh_view import SSHView

            ssh = self.view.query_one(SSHView)

            ssh.cursor_down()

        elif self.focus == "settings":

            from views.settings_view import SettingsView

            settings = self.view.query_one(SettingsView)

            settings.cursor_down()

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

        elif self.focus == "settings":

            from views.settings_view import SettingsView

            settings = self.view.query_one(SettingsView)

            if settings.mode == "menu":

                settings.open()

            else:
                settings.select_option()


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

        elif menu == "Settings":

            self.focus = "settings"

            from views.settings_view import SettingsView

            settings = self.view.query_one(SettingsView)

            settings.focus()

            print("Focus -> Settings")

    def action_left(self):

        self.focus = "sidebar"

        sidebar = self.query_one(Sidebar)

        sidebar.focus()
        print("Focus -> Sidebar")

    def action_disconnect(self):

        if self.focus != "ssh":
            return

        from views.ssh_view import SSHView

        ssh = self.view.query_one(SSHView)

        ssh.disconnect()

        self.focus = "sidebar"

    def action_add_server(self):

        self.app.push_screen(
            AddServerModal()
        )


    def action_delete_server(self):

        self.notify("Delete Server (Coming Soon)")

    def action_edit_server(self):

        menu = self.query_one(Sidebar).current

        if menu != "SSH Manager":
            return

        from views.ssh_view import SSHView

        ssh = self.view.query_one(SSHView)

        self.app.push_screen(
            AddServerModal(
                server=ssh.current,
                index=ssh.selected
            )
        )

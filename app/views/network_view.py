from textual.app import ComposeResult
from textual.widgets import Static
from textual.containers import Horizontal


from controllers.network_controller import NetworkController

from widgets.interface_widget import InterfaceWidget
from widgets.ping_widget import PingWidget
from widgets.route_widget import RouteWidget

class NetworkView(Static):

    def __init__(self):
        super().__init__()

        self.controller = NetworkController()

    def compose(self) -> ComposeResult:

        self.ping = PingWidget()
        self.interface = InterfaceWidget()
        self.routes = RouteWidget()


        with Horizontal():

            yield self.interface
            yield self.ping

        yield self.routes


    def on_mount(self):

        self.refresh_ping()

    def refresh_ping(self):

        data = self.controller.ping("8.8.8.8")
        self.ping.update_ping(data)

        interfaces = self.controller.interfaces()
        self.interface.update_interfaces(interfaces)

        routes = self.controller.routes()
        self.routes.update_routes(routes)


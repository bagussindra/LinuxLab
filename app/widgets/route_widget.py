from textual.widgets import Static


class RouteWidget(Static):

    def update_routes(self, routes):

        text = "[bold cyan]📡 Routing Table[/bold cyan]\n\n"

        for route in routes:

            text += route + "\n"

        self.update(text)

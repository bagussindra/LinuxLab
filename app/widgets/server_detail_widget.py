from textual.widgets import Static


class ServerDetailWidget(Static):

    def show_server(self, server):

        text = "[bold green]Server Detail[/bold green]\n\n"

        text += f"Name : {server['name']}\n"

        text += f"Host : {server['host']}\n"

        text += f"User : {server['user']}\n"

        text += f"Port : {server['port']}\n"

        self.update(text)

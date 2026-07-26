from textual.widgets import Static


class InterfaceWidget(Static):

    def update_interfaces(self, interfaces):

        text = "[bold cyan]🌐 Interfaces[/bold cyan]\n\n"

        for iface in interfaces:

            text += (
                f"[bold]{iface['name']}[/bold]\n"
                f"Status : {iface['state']}\n"
                f"IP     : {iface['ip']}\n\n"
            )

        self.update(text)

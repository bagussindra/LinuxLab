from textual.widgets import Static


class ServerDetailWidget(Static):

    def show_info(self, info):

        text = "[bold green]Server Detail[/bold green]\n\n"

        text += f"Hostname : {info['hostname']}\n"
        text += f"Kernel   : {info['kernel']}\n"
        text += f"Uptime   : {info['uptime']}\n\n"

        text += "Load Average\n"

        text += (
            f"{info['load'][0]}  "
            f"{info['load'][1]}  "
            f"{info['load'][2]}\n\n"
        )

        text += "Memory\n"

        text += info["memory"]

        text += "\nDisk\n"

        text += info["disk"]

        self.update(text)

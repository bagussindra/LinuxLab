import socket
import subprocess

import psutil

from textual.widgets import Static


class NetworkView(Static):

    def on_mount(self):

        self.last = psutil.net_io_counters()

        self.set_interval(1, self.refresh_network)

    def progress_bar(self, percent):

        total = 20

        filled = int(percent / 100 * total)

        return "█" * filled + "░" * (total - filled)

    def refresh_network(self):

        host = socket.gethostname()

        # Cari interface aktif
        interface = "-"

        for name, addrs in psutil.net_if_addrs().items():
            for addr in addrs:
                if (
                    addr.family == socket.AF_INET
                    and not addr.address.startswith("127.")
                ):
                    interface = name
                    break
            if interface != "-":
                break

        # Cari IP dari interface aktif
        ip = "-"

        for addr in psutil.net_if_addrs().get(interface, []):
            if addr.family == socket.AF_INET:
                if not addr.address.startswith("127."):
                    ip = addr.address
                    break

        # Gateway
        gateway = "-"

        try:
            route = subprocess.check_output(
                "ip route | grep default",
                shell=True,
                text=True,
            )

            gateway = route.split()[2]

        except Exception:
            pass

        # DNS
        dns = []

        try:
            with open("/etc/resolv.conf") as f:
                for line in f:
                    if line.startswith("nameserver"):
                        dns.append(line.split()[1])
        except Exception:
            pass

        # Traffic
        now = psutil.net_io_counters()

        upload = now.bytes_sent - self.last.bytes_sent
        download = now.bytes_recv - self.last.bytes_recv

        self.last = now

        up_kb = upload / 1024
        down_kb = download / 1024

        up_percent = min(up_kb / 1000 * 100, 100)
        down_percent = min(down_kb / 1000 * 100, 100)

        text = "🌐 Network\n\n"

        text += f"Hostname     : {host}\n"
        text += f"Interface    : {interface}\n"
        text += f"IPv4         : {ip}\n"
        text += f"Gateway      : {gateway}\n\n"

        text += "DNS\n"

        for server in dns:
            text += f"  {server}\n"

        text += "\n"

        text += "Upload\n"
        text += (
            self.progress_bar(up_percent)
            + f" {up_kb:.1f} KB/s\n\n"
        )

        text += "Download\n"
        text += (
            self.progress_bar(down_percent)
            + f" {down_kb:.1f} KB/s\n\n"
        )

        text += (
            f"RX Total : {now.bytes_recv/1024/1024/1024:.2f} GB\n"
        )

        text += (
            f"TX Total : {now.bytes_sent/1024/1024/1024:.2f} GB\n\n"
        )

        try:
            subprocess.check_output(
                "ping -c1 -W1 8.8.8.8",
                shell=True,
            )

            text += "Internet : 🟢 Connected"

        except Exception:

            text += "Internet : 🔴 Offline"

        self.update(text)

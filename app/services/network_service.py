from services.ssh_service import SSHService
import re

class NetworkService:

    def __init__(self):
        self.ssh = SSHService()

    def ping(self, host="8.8.8.8"):

        output = self.ssh.execute(
            f"ping -c 4 {host}"
        )

        packet = re.search(
            r"(\d+) packets transmitted, (\d+) received,.*?(\d+)% packet loss",
            output,
        )

        latency = re.search(
            r"min/avg/max.*?=\s([\d.]+)/([\d.]+)/([\d.]+)/",
            output,
        )

        return {
            "host": host,
            "sent": int(packet.group(1)) if packet else 0,
            "received": int(packet.group(2)) if packet else 0,
            "loss": int(packet.group(3)) if packet else 100,
            "avg": latency.group(2) if latency else "-",
            "reachable": packet is not None and packet.group(2) != "0",
        }

    def interfaces(self):

        output = self.ssh.execute(
            "ip -br addr"
        )

        interfaces = []

        for line in output.splitlines():

            parts = line.split()

            if len(parts) < 3:
                continue

            interfaces.append({
               "name": parts[0],
               "state": parts[1],
               "ip": parts[2],
            })

        return interfaces

    def routes(self):

        output = self.ssh.execute("ip route")

        routes = []

        for line in output.splitlines():

            routes.append(line)

        return routes

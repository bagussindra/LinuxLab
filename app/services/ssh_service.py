from app.core.ssh_client import SSHClient


class SSHService:

    def __init__(self):
        self.client = SSHClient()
        self.connected = False
        self.server = None

    def connect(self, server):

        self.client.connect(
            host=server["host"],
            username=server["user"],
            password=server["password"],
            port=server["port"],
        )

        self.server = server
        self.connected = True

    def execute(self, command):

        if not self.connected:
            return "Not connected."

        return self.client.execute(command)

    def get_system_info(self):

        return {
            "hostname": self.execute("hostname").strip(),
            "kernel": self.execute("uname -r").strip(),
            "uptime": self.execute("uptime -p").strip(),
            "load": self.execute("cat /proc/loadavg").split()[:3],
            "memory": self.execute("free -h"),
            "disk": self.execute("df -h /"),
        }

    def disconnect(self):

        if self.connected:
            self.client.disconnect()

        self.connected = False
        self.server = None

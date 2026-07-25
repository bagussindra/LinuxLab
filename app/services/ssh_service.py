from core.ssh_client import SSHClient

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

            "os": self.execute(
                "grep PRETTY_NAME /etc/os-release | cut -d= -f2 | tr -d '\"'"
            ).strip(),

            "kernel": self.execute("uname -r").strip(),

            "cpu": self.execute(
                "lscpu | grep 'Model name' | cut -d: -f2"
            ).strip(),

            "uptime": self.execute("uptime -p").strip(),

            "load": " ".join(
            self.execute("cat /proc/loadavg").split()[:3]
            ),

            "memory": self.execute(
                "free -h | awk '/Mem:/ {print $3 \" / \" $2}'"
            ).strip(),

            "disk": self.execute(
                "df -h / | awk 'NR==2 {print $3 \" / \" $2}'"
            ).strip(),

            "ip": self.execute(
                "hostname -I | awk '{print $1}'"
            ).strip(),
        }

    def disconnect(self):

        if self.connected:
            self.client.disconnect()

        self.connected = False
        self.server = None

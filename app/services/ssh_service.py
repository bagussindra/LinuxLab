from core.ssh_client import SSHClient

class SSHService:

    _instance = None


    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

            cls._instance.client = SSHClient()
            cls._instance.connected = False
            cls._instance.server = None

        return cls._instance

    def __init__(self):
        pass

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
                "lscpu | awk -F: '/Model name/ {print $2}' | sed 's/@.*//' | sed 's/Processor//' | sed 's/pc-i440fx.*//' | xargs"
            ).strip(),

            "cpu_usage": self.execute(
                "top -bn1 | grep 'Cpu(s)' | awk '{print int($2)}'"
            ).strip(),

            "uptime": self.execute("uptime -p").strip(),

            "load": " ".join(
            self.execute("cat /proc/loadavg").split()[:3]
            ),

            "memory": self.execute(
                "free -h | awk '/Mem:/ {print $3 \" / \" $2}'"
            ).strip(),
            "memory_usage": self.execute(
                "free | awk '/Mem:/ {print int($3/$2*100)}'"
            ).strip(),

            "disk": self.execute(
                "df -h / | awk 'NR==2 {print $3 \" / \" $2}'"
            ).strip(),
            "disk_usage": self.execute(
                "df / | awk 'NR==2 {gsub(/%/, \"\", $5); print $5}'"
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

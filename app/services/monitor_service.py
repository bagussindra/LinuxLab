from services.ssh_service import SSHService


class MonitorService:

    def __init__(self):
        self.ssh = SSHService()

    def status(self):

        if not self.ssh.connected:
            return {

                "ssh": False,

                "cpu": False,
                "cpu_usage": 0,

                "memory": False,
                "memory_usage": 0,

                "disk": False,
                "disk_usage": 0,

                "internet": False,
                "docker": False,
                "nginx": False,

            }

        info = self.ssh.get_system_info()

        cpu = int(info["cpu_usage"])
        mem = int(info["memory_usage"])
        disk = int(info["disk_usage"])

        return {
            "ssh": self.ssh.connected,

            "cpu": cpu < 80,
            "cpu_usage": cpu,

            "memory": mem < 80,
            "memory_usage": mem,

            "disk": disk < 90,
            "disk_usage": disk,

            "internet": self.internet(),
            "docker": self.service_active("docker"),
            "nginx": self.service_active("nginx"),
        }

    def service_active(self, service: str):

        status = self.ssh.execute(
            f"systemctl is-active {service}"
        ).strip()

        if status == "active":
            return True

        return False

    def internet(self):

        result = self.ssh.execute(
            "ping -c 1 -W 1 8.8.8.8 >/dev/null && echo OK || echo FAIL"
        ).strip()

        return result == "OK"

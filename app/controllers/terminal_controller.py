from services.ssh_service import SSHService


class TerminalController:

    def __init__(self):

        self.ssh = SSHService()

    def execute(self, command):

        return self.ssh.execute(command)

    def prompt(self):

        hostname = self.ssh.execute("hostname").strip()

        return f"root@{hostname}:~#"

from services.ssh_service import SSHService


class SSHController:

    def __init__(self):

        self.service = SSHService()

    def connect(self, server):

        self.service.connect(server)

        return self.service.get_system_info()

from services.ssh_service import SSHService


class SSHController:

    def __init__(self):

        self.service = SSHService()

    def connect(self, server):

        if (
            not self.service.connected
            or self.service.server != server
        ):
            self.service.connect(server)

        return self.service.get_system_info()

    def disconnect(self):

        self.service.disconnect()

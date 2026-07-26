from services.network_service import NetworkService


class NetworkController:

    def __init__(self):
        self.service = NetworkService()

    def ping(self, host="8.8.8.8"):

        return self.service.ping(host)

    def interfaces(self):

        return self.service.interfaces()

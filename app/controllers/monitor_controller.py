from services.monitor_service import MonitorService


class MonitorController:

    def __init__(self):

        self.service = MonitorService()

    def status(self):

        return self.service.status()

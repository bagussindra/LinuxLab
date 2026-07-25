from services.settings_service import SettingsService


class SettingsController:

    def __init__(self):
        self.service = SettingsService()

    def get(self, key):
        return self.service.get(key)

    def set(self, key, value):
        self.service.set(key, value)

    def all(self):
        return self.service.all()

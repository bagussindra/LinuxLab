from config.settings import SETTINGS


class SettingsService:

    def get(self, key):
        return SETTINGS.get(key)

    def set(self, key, value):
        SETTINGS[key] = value

    def all(self):
        return SETTINGS

import json
from pathlib import Path


class ServerService:

    FILE = Path("app/config/servers.json")

    def load(self):

        if not self.FILE.exists():
            return []

        with open(self.FILE, "r") as f:
            return json.load(f)

    def save(self, servers):

        with open(self.FILE, "w") as f:
            json.dump(
                servers,
                f,
                indent=4
            )

    def add(self, server):

        servers = self.load()
        servers.append(server)
        self.save(servers)

    def delete(self, index):

        servers = self.load()

        if 0 <= index < len(servers):
            servers.pop(index)

        self.save(servers)

    def update(self, index, server):

        servers = self.load()

        if 0 <= index < len(servers):
            servers[index] = server

        self.save(servers)

from app.services.ssh_service import SSHService
import json


def main():

    with open("config/servers.json") as f:
        servers = json.load(f)

    server = servers[0]

    ssh = SSHService()

    print("Connecting...")

    ssh.connect(server)

    print("Connected")

    print()

    print(
        ssh.execute("hostname")
    )

    print(
        ssh.execute("uptime")
    )

    ssh.disconnect()

    print("Disconnected")


if __name__ == "__main__":
    main()

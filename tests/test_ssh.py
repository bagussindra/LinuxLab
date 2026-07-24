from app.services.ssh_service import SSHService
import json


def main():

    with open("config/servers.json") as f:
        servers = json.load(f)

    server = servers[0]

    ssh = SSHService()

    print("Connecting...")

    ssh.connect(server)

    print("Connected\n")

    info = ssh.get_system_info()

    print("=" * 40)
    print("SERVER INFORMATION")
    print("=" * 40)

    print(f"Hostname : {info['hostname']}")
    print(f"Kernel   : {info['kernel']}")
    print(f"Uptime   : {info['uptime']}")
    print(f"Load Avg : {' '.join(info['load'])}")

    print("\n========== MEMORY ==========\n")
    print(info["memory"])

    print("\n========== DISK ==========\n")
    print(info["disk"])

    ssh.disconnect()

    print("\nDisconnected")


if __name__ == "__main__":
    main()

import paramiko


class SSHClient:

    def __init__(self):
        self.client = None

    def connect(self, host, username, password, port=22):

        self.client = paramiko.SSHClient()

        self.client.set_missing_host_key_policy(
            paramiko.AutoAddPolicy()
        )

        self.client.connect(
            hostname=host,
            username=username,
            password=password,
            port=port,
            timeout=5
        )

    def execute(self, command):

        stdin, stdout, stderr = self.client.exec_command(command)

        output = stdout.read().decode()
        error = stderr.read().decode()

        return output + error

    def disconnect(self):

        if self.client:
            self.client.close()

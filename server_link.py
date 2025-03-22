class Server:
    ip_count = 1

    def __init__(self, router):
        self.buffer = []
        self.ip = Server.ip_count
        Server.ip_count += 1
        self.router = router

    def send_data(self, data):
        self.router.receive_data(data)

    def get_data(self):
        received_data = self.buffer.copy()
        self.buffer.clear()
        return received_data

    def get_ip(self):
        return self.ip


class Router:
    def __init__(self):
        self.buffer = []
        self.servers = []

    def receive_data(self, data):
        self.buffer.append(data)

    def link(self, server):
        self.servers.append(server)

    def unlink(self, server):
        self.servers.remove(server)

    def send_data(self):
        for data in self.buffer:
            destination_ip = data.ip
            for server in self.servers:
                if server.get_ip() == destination_ip:
                    server.buffer.append(data)
        self.buffer.clear()


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip

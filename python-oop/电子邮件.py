class Email:
    def __init__(self, msg: str, sender, recipient_name: str):
        self.msg = msg
        self.sender = sender
        self.recipient_name = recipient_name


class Server:
    def __init__(self):
        self.clients = {}
    def send(self, email: Email):
        self.clients[email.recipient_name].inbox.append(email)
    def register_client(self, client):
        self.clients[client.name] = client


class Client:
    def __init__(self, server: Server, name: str):
        self.inbox: list = []
        self.server = server
        self.name = name
        server.register_client(self)

    def compose(self, message: str, recipient_name: str):
        email = Email(message, self, recipient_name)
        self.server.send(email)
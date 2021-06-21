from random import randint
from datetime import datetime


class Client:
    def __init__(self, login):
        self.token = 0
        self.login = login

    def login_to_system(self):
        self.token = randint(0, 1000000000)
        return self.token

    def logout(self):
        self.token = 0


class Message:
    def __init__(self, sender, receiver, message):
        self.sender = sender
        self.receiver = receiver
        self.message = message
        self.send_date = datetime.now()


class GlobalServer:
    def __init__(self):
        self.clients = []
        self.messages = {}

    def add_client(self, login: str):
        if self.get_client(login) is not None:
            return False
        self.clients.append(Client(login))
        return True

    def get_client(self, login):
        return next((client for client in self.clients if client.login == login), None)

    def get_client_token(self, token):
        if token <= 0:
            return None
        return next((client for client in self.clients if client.token == token), None)

    def list_clients(self):
        return list(map(lambda d: d.login, self.clients))

    def send_message(self, token: int, receiver: str, message: str):
        sender = self.get_client_token(token)
        if sender is None:
            return 1
        if receiver is not None:
            target = self.get_client(receiver)
            if target is None:
                return 2
            if receiver in self.messages.keys():
                list_mess = self.messages[receiver]
            else:
                list_mess = []
            list_mess.append(Message(sender.login, receiver, message))
            self.messages[receiver] = list_mess
        else:
            for client in self.clients:
                receiver = client.login
                if receiver != sender.login:
                    if receiver in self.messages.keys():
                        list_mess = self.messages[receiver]
                    else:
                        list_mess = []
                    list_mess.append(Message(sender.login, receiver, message))
                    self.messages[receiver] = list_mess

        return 0

    def get_all_messages(self, token: int, target_login: str = None):
        user = self.get_client_token(token)
        if user is None:
            return 1
        if user.login not in self.messages.keys():
            return 0

        if target_login is not None:
            messages = list(filter(lambda d: d.sender == target_login, self.messages[user.login]))
        else:
            messages = list(self.messages[user.login])

        for e in messages:
            self.messages[user.login].remove(e)
        if len(self.messages[user.login]) == 0:
            del self.messages[user.login]
        return messages


GLOBAL_SERVER = GlobalServer()

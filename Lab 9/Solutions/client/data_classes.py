import datetime


class User:
    def __init__(self, id: str, name: str, last_active: str):
        self.id = id
        self.name = name
        self.password = ""
        self.last_active = last_active

    @classmethod
    def fromDict(cls, data):
        return cls(data["id"], data["attributes"]["name"], data["attributes"]["last_active"])


class Message:

    def __init__(self, id: str, content: str, sender_id, receiver_id):
        self.receiver_id = receiver_id
        self.sender_id = sender_id
        self.id = id
        self.content = content

    def __hash__(self):
        return hash(self.id)

    @classmethod
    def fromDict(cls, data):
        id_ = data['id']
        content_ = data["attributes"]["content"]
        user_id_ = data["attributes"]["from_user_id"]
        to_user_id_ = data["attributes"]["to_user_id"]
        message = Message(id_, content_, user_id_, to_user_id_)
        return message

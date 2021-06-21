import datetime
from typing import Optional, List, Dict


class User:
    def __init__(self, id: str, name: str, logged: str, icon_number: int):
        self.id = id
        self.name = name
        self.password = ""
        self.logged = logged
        self.icon_number = icon_number

    @classmethod
    def fromDict(cls, data):
        return cls(data["id"], data["attributes"]["name"], data["attributes"]["logged"],
                   data["attributes"]["icon_number"])


class Message:
    def __init__(self, id: str, content: str, send_date: str, user_id: str, conversation_id: str):
        self.id = id
        self.content = content
        self.conversation_id = conversation_id
        self.user_id = user_id
        self.send_date = send_date
        self.status_users = []

    def __hash__(self):
        return hash(self.id)

    @classmethod
    def fromDict(cls, data):
        id_ = data['id']
        content_ = data["attributes"]["content"]
        user_id_ = data["attributes"]["user_id"]
        conversation_id_ = data["attributes"]["conversation_id"]
        send_date_ = data["attributes"]["send_date"]
        message = Message(id_, content_, send_date_, user_id_, conversation_id_)
        return message


class Membership:
    def __init__(self, id: str, user_id: str, conversation_id: str, last_download: str, not_read_messages: list):
        self.id = id
        self.not_read_messages = not_read_messages
        self.user_id = user_id
        self.conversation_id = conversation_id
        self.last_download = last_download

    @classmethod
    def fromDict(cls, data):
        return cls(data["id"], data["attributes"]["user_id"], data["attributes"]["conversation_id"],
                   data["attributes"]["last_download"], data["attributes"]["not_read_messages"])


class Conversation:
    def __init__(self, id: str, name: str, users_ids: [] = [], last_active=None):
        self.last_active = last_active if last_active is not None else datetime.datetime.now().strftime(
            '%Y-%m-%d %H:%M:%S')
        self.users_ids = users_ids
        self.id = id
        self.name = name
        self.memberships: Dict[str, Membership] = {}
        self.messages: List[Message] = []

    def online_users(self, users: Dict[str, User]):
        online_users_number_ids = []

        for user_id in self.users_ids:
            if user_id in users.keys():
                if users[user_id].logged:
                    online_users_number_ids.append(user_id)

        return online_users_number_ids

    @classmethod
    def fromDict(cls, data):
        return cls(data["id"], data["attributes"]["name"], data["attributes"]["users_ids"],
                   data["attributes"]["last_active"])

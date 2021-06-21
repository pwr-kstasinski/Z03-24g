import json

from PyQt5.QtCore import QObject, pyqtSignal, QRunnable, QThreadPool

import data_classes
from messages_api_4.openapi_client.api.conversations_api import ConversationsApi
from messages_api_4.openapi_client.api.memberships_api import MembershipsApi
from messages_api_4.openapi_client.api.messages_api import MessagesApi
from messages_api_4.openapi_client.api.users_api import UsersApi
from messages_api_4.openapi_client.model.conversation_inst1 import ConversationInst
from messages_api_4.openapi_client.model.membership_inst1 import MembershipInst
from messages_api_4.openapi_client.model.message_inst1 import MessageInst
from messages_api_4.openapi_client.model.user_inst1 import UserInst

users_api = UsersApi()
messages_api = MessagesApi()
memberships_api = MembershipsApi()
conversations_api = ConversationsApi()

apis = [users_api, messages_api, memberships_api, conversations_api]


def set_name_and_password(name, password):
    for api in apis:
        api.api_client.configuration.username = name
        api.api_client.configuration.password = password


def clear_name_and_password():
    set_name_and_password(None, None)


class ProcessRunnableStatus(QObject):
    captureDataFinished = pyqtSignal(dict)


class ProcessRunnable(QRunnable):
    def __init__(self, target):
        QRunnable.__init__(self)
        self.t = target
        self.status = ProcessRunnableStatus()

    def run(self):
        t = self.t()
        # noinspection PyUnresolvedReferences
        self.status.captureDataFinished.emit(t)

    def start(self):
        QThreadPool.globalInstance().start(self)


def do_async(callback, fun):
    p = ProcessRunnable(fun)
    connect_callback_and_start(callback, p)


def connect_callback_and_start(callback, p: QRunnable):
    p.status.captureDataFinished.connect(callback)
    p.start()


def async_load_users(callback):
    def get_users():
        users = users_api.get_users()
        data = users.data
        return {"users": data}

    do_async(lambda data: callback(data["users"]), get_users)


def async_register_user(callback, name, password, icon_number):
    def register():
        user = UserInst(data={
            "attributes": {
                "name": name,
                "id": "123",
                "password": password,
                "icon_number": icon_number
            },
            "type": "User"
        })
        created_user = users_api.create_user(post_body=user)
        data = created_user.data
        return data

    do_async(callback, register)


def async_get_user_with_name(callback, name):
    def filter_user():
        users = users_api.get_users(
            filter=json.dumps(
                [{"name": "name", "op": "eq", "val": name}]
            ),
            include="memberships"
        )
        data = {"users": users.data, "memberships": users.included}
        return data

    do_async(callback, filter_user)


def async_load_user_memberships(callback, user_id):
    def get_memberships_for_user_id():
        messages = users_api.get_memberships(user_id=user_id)
        data = messages.data
        return {"data": data}

    do_async(lambda data: callback(data), get_memberships_for_user_id)


def async_load_conversation_memberships(callback, conversation_id):
    def filter_memberships():
        memberships = conversations_api.get_memberships(conversation_id=conversation_id)
        data = {"data": memberships.data}
        return data

    do_async(callback, filter_memberships)


def async_create_membership(callback, membership: data_classes.Membership):
    def create_conversation():
        c = MembershipInst(data={
            "attributes": {
                "conversation_id": membership.conversation_id,
                "user_id": membership.user_id,
                "last_download": membership.last_download
            },
            "type": "Membership"
        })
        membership_data = memberships_api.create_membership(post_body=c)
        data = membership_data
        return {"data": data}

    do_async(callback, create_conversation)


def async_get_conversation_with_name(callback, name):
    def filter_user():
        conversations = conversations_api.get_conversations(
            filter=json.dumps(
                [{"name": "name", "op": "eq", "val": name}]
            )
        )
        data = {"data": conversations.data}
        return data

    do_async(callback, filter_user)


def async_get_conversations(callback, user_id):
    def get_conversations_for_user_id():
        messages = users_api.get_conversations(user_id=user_id)
        data = messages.data
        return {"data": data}

    do_async(lambda data: callback(data), get_conversations_for_user_id)


def async_create_conversation(callback, conversation_name: str):
    def create_conversation():
        c = ConversationInst(data={
            "attributes": {
                "name": conversation_name
            },
            "type": "Conversation"
        })
        conversation_data = conversations_api.create_conversation(post_body=c)
        data = conversation_data
        return {"data": data}

    do_async(callback, create_conversation)


def async_load_conversation(callback, conversation_id):
    def get_conversations_for_user_id():
        conversation = conversations_api.get_conversation(conversation_id=conversation_id)
        data = conversation.data
        return {"data": data}

    do_async(lambda data: callback(data), get_conversations_for_user_id)


def async_load_conversation_messages(callback, conversation_id):
    def get_messages_for_conversation_id():
        conversation = conversations_api.get_messages(conversation_id=conversation_id)
        data = conversation.data
        return {"data": data}

    do_async(lambda data: callback(data), get_messages_for_conversation_id)


def async_load_conversation_users(callback, conversation_id):
    def get_users_for_conversation_id():
        conversation = conversations_api.get_users(conversation_id=conversation_id)
        data = conversation.data
        return {"data": data}

    do_async(lambda data: callback(data), get_users_for_conversation_id)


def async_send_message(callback, message: data_classes.Message):
    def send_message():
        m = MessageInst(data={
            "attributes": {
                "content": message.content,
                "user_id": message.user_id,
                "conversation_id": message.conversation_id,
                "send_date": message.send_date
            },
            "type": "Message"
        })
        message_data = messages_api.create_message(post_body=m)
        data = message_data
        return {"data": data}

    do_async(callback, send_message)

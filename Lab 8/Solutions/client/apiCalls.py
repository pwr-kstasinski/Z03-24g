import json
import time

from PyQt5 import sip
from PyQt5.QtCore import QObject, pyqtSignal, QRunnable, QThreadPool

from messages_api.openapi_client.api.messages_api import MessagesApi
from messages_api.openapi_client.api.users_api import UsersApi
from messages_api.openapi_client.model import user_inst1, message_inst1
from beta_api.api.openapi_client.api.users_api import UsersApi as TestUsersApi

import data_classes

user_api = UsersApi()
messages_api = MessagesApi()

test_user_api = TestUsersApi()


class ProcessRunnableStatus(QObject):
    captureDataFinished = pyqtSignal(dict)


class ProcessRunnable(QRunnable):
    def __init__(self, target):
        QRunnable.__init__(self)
        self.t = target
        self.status = ProcessRunnableStatus()

    def run(self):
        t = self.t()
        self.status.captureDataFinished.emit(t)

    def start(self):
        QThreadPool.globalInstance().start(self)


class ProcessRunnableRepeatly(QRunnable):
    def __init__(self, target, seconds, stopWhen):
        QRunnable.__init__(self)
        self.stopWhen = stopWhen
        self.seconds = seconds
        self.t = target
        self.status = ProcessRunnableStatus()

    def run(self):
        while not self.stopWhen():
            t = self.t()
            if not sip.isdeleted(self.status):
                self.status.captureDataFinished.emit(t)
            time.sleep(self.seconds)

    def start(self):
        QThreadPool.globalInstance().start(self)


def repeat_async(seconds, stopWhen, callback, fun):
    p = ProcessRunnableRepeatly(fun, seconds, stopWhen)
    connect_callback_and_start(callback, p)


def do_async(callback, fun):
    p = ProcessRunnable(fun)
    connect_callback_and_start(callback, p)


def connect_callback_and_start(callback, p: QRunnable):
    p.status.captureDataFinished.connect(callback)
    p.start()


def async_load_users(callback):
    def get_users():
        users = user_api.get_all_users()
        data = users.data
        return {"users": data}

    do_async(lambda data: callback(data["users"]), get_users)


def repeat_async_load_users(callback, stopWhen):
    def get_users():
        users = user_api.get_all_users()
        data = users.data
        return {"users": data}

    repeat_async(2, stopWhen, lambda data: callback(data["users"]), get_users)


def repeat_async_load_user_messages(callback, userId, stopWhen):
    def get_user_messages():
        messages = user_api.get_incoming_messages(user_id=userId)
        data = messages.data
        return {"messages": data}

    repeat_async(2, stopWhen, lambda data: callback(data["messages"]), get_user_messages)


def async_register_user(callback, name, password):
    def register():
        user = user_inst1.UserInst1(data={
            "attributes": {
                "name": name,
                "id": "123",
                "password": password
            },
            "type": "User"
        })
        created_user = user_api.create_user(post_body=user)
        data = created_user.data
        return data

    do_async(callback, register)


def async_login_user(callback, name, password):
    def login():
        """meta_login = UserLogin(method="login", args={"name": name, "password": password})
        post_user_login_inst = PostUserLogin(meta=meta_login)
        users = test_user_api.loginuser0(
            post_user_login=post_user_login_inst
            #filter=json.dumps([{"name": "name", "op": "eq", "val": name}, {"name": "password", "op": "eq", "val": password}])
        )"""
        users = user_api.get_all_users(
            filter=json.dumps(
                [{"name": "name", "op": "eq", "val": name}, {"name": "password", "op": "eq", "val": password}])
        )
        data = {"users": users.data}
        return data

    do_async(callback, login)


def async_load_messages(callback, user_id):
    def get_messages_for_user_id():
        messages = user_api.get_incoming_messages(user_id=user_id)
        data = messages.data
        return {"data": data}

    do_async(lambda data: callback(data["data"]), get_messages_for_user_id)


def async_delete_message(callback, message_id):
    def delete_message():
        message = messages_api.delete_message(message_id=message_id)
        print(message)
        return {"data": message}

    do_async(callback, delete_message)


def async_send_message(callback, message: data_classes.Message):
    def send_message():
        m = message_inst1.MessageInst1(data={
            "attributes": {
                "content": message.content,
                "from_user_id": message.sender_id,
                "to_user_id": message.receiver_id
            },
            "type": "Message"
        })
        message_data = messages_api.create_message(post_body=m)
        data = message_data
        return {"data": data}

    do_async(callback, send_message)

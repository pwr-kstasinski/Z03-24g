import asyncio
import datetime
import json
import logging
import time
from typing import Dict

import websockets
from PyQt5.QtCore import pyqtSignal
from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy
from websockets import exceptions
import threading
import safrs

db = SQLAlchemy()
auth = HTTPBasicAuth()

logging.basicConfig(level=logging.NOTSET)
log = logging.getLogger("server")

ID_COLUMN_TYPE = db.String(36)

MAX_ONLINE_DIFFERENCE = 120

from queue import Queue


class Session:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.queue = Queue(maxsize=100)
        self.lock = threading.Lock()


sessions: Dict[str, Session] = {}


@auth.verify_password
def verify_password(username_or_token, password):
    if request.method == "POST" and request.url_rule.rule == "/Users/":
        return True
    query = User.query.filter_by(name=username_or_token, _password=password)
    user: User = query.first()
    if user is None:
        return False

    if request.url_rule.rule == '/Conversations/<string:ConversationId>/messages':
        conversation_id = request.view_args["ConversationId"]
        membership = list(filter(lambda m: m.conversation_id == conversation_id, user.memberships))
        if len(membership) == 1:
            membership[0].last_download = datetime.datetime.now()
    return True


class User(safrs.SAFRSBase, db.Model):
    """
        description: User description
    """
    __tablename__ = 'Users'
    http_methods = ["get", "post", "delete"]
    custom_decorators = [auth.login_required]

    id = db.Column(ID_COLUMN_TYPE, primary_key=True)
    _password = db.Column(db.String(30))
    name = db.Column(db.String(30), unique=True)
    logged = db.Column(db.Boolean, default=False)

    memberships = db.relationship("Membership")
    memberships.http_methods = ["get"]

    conversations = db.relationship("Conversation", secondary="Memberships",
                                    primaryjoin="Membership.user_id == User.id",
                                    secondaryjoin="Conversation.id == Membership.conversation_id",
                                    viewonly=True)
    conversations.http_methods = ["get"]

    @safrs.jsonapi_attr
    def password(self):
        """---
            "_password" is hidden because of the "_" prefix, provide a custom attribute "password" the Person fields
        """
        return "hidden"

    @password.setter
    def password(self, val):
        """
            Allow setting _password
        """
        self._password = val


@db.event.listens_for(User, "after_insert")
def insert_user_event_handler(mapper, connection, target):
    try:
        data_dict = target._s_jsonapi_encode()
        add_to_queues(json.dumps(data_dict))
    except RuntimeError:
        print("user runtime error insert user handler")


@db.event.listens_for(User.logged, "set")
def logged_change_user_event_handler(target, value, oldvalue, initiator):
    try:
        attributes = target.to_dict() # ._s_jsonapi_encode()
        attributes["logged"] = not oldvalue
        add_to_queues(json.dumps({"attributes": attributes, "id": target.id, "type": "User"}))
    except RuntimeError as e:
        print("user runtime error logged change handler")


def add_to_queues(data: str):
    for session in sessions.values():
        with session.lock:
            session.queue.put(data)


class Conversation(safrs.SAFRSBase, db.Model):
    """
        description: Conversation description
    """
    __tablename__ = 'Conversations'
    http_methods = ["get", "post", "delete"]
    custom_decorators = [auth.login_required]

    id = db.Column(ID_COLUMN_TYPE, primary_key=True)
    name = db.Column(db.String(30))

    messages = db.relationship("Message")  # , lazy='dynamic')
    messages.http_methods = ["get"]

    users = db.relationship("User", secondary="Memberships",
                            primaryjoin="Conversation.id == Membership.conversation_id",
                            secondaryjoin="Membership.user_id == User.id",
                            viewonly=True,
                            lazy='dynamic')
    users.http_methods = ["get"]

    @safrs.jsonapi_attr
    def users_ids(self):
        return list(map(lambda u: u.id, self.users.all()))

    @safrs.jsonapi_attr
    def last_active(self):
        if not isinstance(self.messages, list):
            return
        messages_all = self.messages
        if len(messages_all) == 0:
            return
        last_active = messages_all[0].send_date
        for message in messages_all:
            send_date = message.send_date
            if send_date > last_active:
                last_active = send_date
        return last_active


class Membership(safrs.SAFRSBase, db.Model):
    """
        description: Membership description
    """
    __tablename__ = 'Memberships'
    http_methods = ["get", "post", "delete"]
    custom_decorators = [auth.login_required]

    _user_id = db.Column(ID_COLUMN_TYPE, db.ForeignKey("Users.id"), primary_key=True)
    _conversation_id = db.Column(ID_COLUMN_TYPE, db.ForeignKey("Conversations.id"), primary_key=True)
    last_download = db.Column(db.DateTime, default=lambda: datetime.datetime.now())

    @safrs.jsonapi_attr
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, val):
        self._user_id = val

    @safrs.jsonapi_attr
    def conversation_id(self):
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, val):
        self._conversation_id = val

    @safrs.jsonapi_attr
    def not_read_messages(self):
        not_read_messages_ids = []
        conversation = Conversation.query.filter_by(id=self._conversation_id).first()

        if isinstance(self.last_download, datetime.datetime):
            for message in conversation.messages:
                if message.user_id != self._user_id:
                    if isinstance(message.send_date, datetime.datetime):
                        if message.send_date > self.last_download:
                            not_read_messages_ids.append(message.id)

        return not_read_messages_ids


class Message(safrs.SAFRSBase, db.Model):
    """
        description: Message description
    """
    __tablename__ = 'Messages'
    custom_decorators = [auth.login_required]
    http_methods = ["get", "post"]

    id = db.Column(ID_COLUMN_TYPE, primary_key=True)
    content = db.Column(db.String(300))
    send_date = db.Column(db.DateTime, default=datetime.datetime.now)

    user_id = db.Column(ID_COLUMN_TYPE, db.ForeignKey("Users.id"), nullable=False)
    conversation_id = db.Column(ID_COLUMN_TYPE, db.ForeignKey("Conversations.id"), nullable=False)


@db.event.listens_for(Message, "after_insert")
def insert_message_event_handler(mapper, connection, target):
    try:
        data_dict = target._s_jsonapi_encode()
        for session in sessions.values():
            membership = Membership.query.filter_by(_user_id=session.user_id, _conversation_id=target.conversation_id).first()
            membership.last_download = datetime.datetime.now()
        add_to_queues(json.dumps(data_dict))
    except RuntimeError:
        print("message runtime error insert message handler")


HOST = "localhost"
API_PORT = 5000
WS_PORT = 8765
SERVER_NAME = f"{HOST}:{API_PORT}"
app = Flask("Messages server")
username = "root"
password = "my-secret-pw"
server = "localhost"
db_name = "messages"
db_uri = f"mysql+mysqlconnector://{username}:{password}@{server}/{db_name}"
app.config.update(SQLALCHEMY_DATABASE_URI=db_uri, DEBUG=True)  # , SERVER_NAME=SERVER_NAME)
db.init_app(app)
db.app = app
db.create_all()
API_PREFIX = ""

DEFAULT_MESSAGE = "ping"


async def echo(websocket, path):
    user_id = None
    user = None
    try:
        user_id = await websocket.recv()
        user = db.session.query(User).filter_by(id=user_id).first()
        session = Session(user_id)
        sessions[user_id] = session
        user.logged = True
        db.session.add(user)
        db.session.commit()
        while True:
            data = DEFAULT_MESSAGE
            with session.lock:
                if not session.queue.empty():
                    data = session.queue.get()
            log.info(f"websocket sent data: {data}")
            await websocket.send(json.dumps(data))
            if data == DEFAULT_MESSAGE:
                await asyncio.sleep(3)
    except exceptions.ConnectionClosedOK:
        log.info(f"websocket connection closed")
    except exceptions.ConnectionClosedError:
        log.info(f"websocket connection force closed ")
    if user_id is not None and user_id in sessions.keys():
        sessions.pop(user_id)
        if user is not None:
            user.logged = False
            db.session.add(user)
            db.session.commit()


with app.app_context():
    custom_swagger = {
        "securityDefinitions": {
            "BasicAuth": {"type": "basic"}
        },
        "security": [{"BasicAuth": []}],
    }

    safrs_api = safrs.SAFRSAPI(
        app,
        host=HOST,
        port=API_PORT,
        prefix=API_PREFIX,
        custom_swagger=custom_swagger
    )

    user = User.query.filter_by(name="test1").first()
    if user is None:
        user1 = User(name="test1", _password="test2")
        user2 = User(name="test2", _password="test2")
        conversation = Conversation(name="Everyone")
        Membership(user_id=user1.id, conversation_id=conversation.id)
        Membership(user_id=user2.id, conversation_id=conversation.id)
        Message(user_id=user1.id, content="test message", conversation_id=conversation.id)

    safrs_api.expose_object(User)
    safrs_api.expose_object(Conversation)
    safrs_api.expose_object(Membership)
    safrs_api.expose_object(Message)

    print("Starting API: http://{}:{}{}".format(HOST, API_PORT, API_PREFIX))
    threading.Thread(target=lambda: app.run(host=HOST, port=API_PORT, debug=True, use_reloader=False)).start()

    print(f"Starting websocket: ws://{HOST}:{WS_PORT}")
    asyncio.get_event_loop().run_until_complete(websockets.serve(echo, 'localhost', 8765))
    asyncio.get_event_loop().run_forever()

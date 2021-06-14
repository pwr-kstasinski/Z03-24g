from flask import Flask
from flask.globals import request
from flask.helpers import make_response 
from flask_socketio import SocketIO, emit, ConnectionRefusedError
import os
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import or_

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app, cors_allowed_origins='*')
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{os.environ["DB_USER"]}:{os.environ["DB_PASS"]}@{os.environ["DB_HOST"]}/{os.environ["DB_NAME"]}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
marshmallow = Marshmallow(app)

class Users(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(30), nullable=False)
    online = db.Column(db.Boolean, nullable=False)

    def __init__(self, username, password, online = False):
        self.username = username
        self.password = password
        self.online = online


class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(80), nullable=False)
    receiver = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(2000), nullable=False)
    is_read = db.Column(db.Boolean, nullable=False)
    datetime = db.Column(db.String, nullable=False)

    def __init__(self, sender, receiver, content, datetime=0):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_read = False
        self.datetime = datetime

class GeneralMessages (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(2000), nullable=False)
    datetime = db.Column(db.String, nullable=False)

    def __init__(self, sender, content, datetime):
        self.sender = sender
        self.content = content
        self.datetime = datetime

class UsersSchema(marshmallow.Schema):
    class Meta:
        fields = ('username', 'online')


class UsersSchemaPass(marshmallow.Schema):
    class Meta:
        fields = ('username', 'password', 'online')

users_schema = UsersSchema(many=True)
users_schema_pass = UsersSchemaPass(many=True)


class MessageSchema(marshmallow.Schema):
    class Meta:
        fields = ('sender', 'receiver', 'content', 'is_read', 'datetime')

message_schema = MessageSchema(many=True)


class GeneralMessageSchema(marshmallow.Schema):
    class Meta:
        fields = ('sender', 'content', 'datetime')

general_schema = GeneralMessageSchema(many=True)


@socketio.on('message')
def handleMessage(message_data):
    db.session.add(Messages(message_data['sender'], message_data['receiver'], message_data['content'], message_data['datetime']))
    db.session.commit()
    sendMessageToUser(message_data)
    # send(message_data, broadcast=True)

logged_users = []

def searchLoggedUsers(username):
    ids = []
    for user in logged_users:
        if user["username"] == username:
            ids.append(user["id"])
    return ids

def sendMessageToUser(message_data):
    sender = searchLoggedUsers(message_data["sender"])
    destination = searchLoggedUsers(message_data["receiver"])
    if (not destination):
        message_data['is_read'] = False
        for user in sender:
            emit('message', message_data, to=user)
    elif (destination and destination != sender):
        message_data['is_read'] = True
        for user in sender:
            emit('message', message_data, to=user)
        for user in destination:
            emit('message', message_data, to=user)
    else:
        message_data['is_read'] = True
        for user in sender:
            emit('message', message_data, to=user)
        

@socketio.on('login')
def login(data):
    user = users_schema_pass.dump(Users.query.filter_by(username=data["username"]))
    print(user)
    if(not user):
        emit('login', 'username not found')
    if(user[0]['password'] == data["password"]):
        Users.query.filter_by(username=data["username"]).update({Users.online: True}, synchronize_session=False)
        db.session.commit()
        sendUsers()
        logged_users.append({"username":data["username"], "id": request.sid})
        print(logged_users)
        return emit('login', ['Login successful', getAllPrivateMessages(data["username"]), getGeneralMessages()])
    emit('login', 'wrong password')

def getAllPrivateMessages(username):
    Messages.query.filter_by(receiver=username).update({Messages.is_read: True}, synchronize_session=False)
    db.session.commit()
    return message_schema.dump(Messages.query.filter(or_(Messages.sender==username, Messages.receiver==username)))

def getGeneralMessages():
    return general_schema.dump(GeneralMessages.query)

@socketio.on('logout')
def logout(data):
    user = users_schema_pass.dump(Users.query.filter_by(username=data["username"]))
    if(not user):
        raise ConnectionRefusedError
    if(user[0]['password'] == data["password"]):
        Users.query.filter_by(username=data["username"]).update({Users.online: False}, synchronize_session=False)
        db.session.commit()
        logged_users.remove({"username":data["username"], "id": request.sid})
        print(logged_users)
        sendUsers()
        return emit('logout', 'Logout_successful')
    raise ConnectionRefusedError


@socketio.on('register')
def register(data):
    if not data["username"] or not data["password"]:
        return emit('register', 'Incorrect data')
    user = users_schema_pass.dump(Users.query.filter_by(username=data["username"]))
    if user:
        return emit('register', 'Username already exists')
    db.session.add(Users(data["username"], data['password']))
    db.session.commit()
    sendUsers()
    return emit('register', 'Registration succesful. You may now log in')

@socketio.on('users')
def sendUsers():
    users = users_schema.dump(Users.query)
    print("uzytkownicy:" + str(users))
    emit('users', users, broadcast=True)

@socketio.on('general')
def generalMessage(message_data):
    db.session.add(GeneralMessages(message_data['sender'], message_data['content'], message_data['datetime']))
    db.session.commit()
    for user in logged_users:
        emit('general', message_data, to=user['id'])

isHealthy = True

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    if isHealthy:
        return(make_response("Server is healthy", 200))
    return(make_response("Server is unhealthy", 500))

@app.route("/set-unhealthy", methods=['GET'])
def set_unhealthy():
    global isHealthy
    isHealthy = False
    return(make_response("You make me sick", 200))


if __name__ == '__main__':
	socketio.run(app, debug=True)

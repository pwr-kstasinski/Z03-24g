from enum import unique
from typing import Text
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from safrs import SAFRSBase, SAFRSAPI, jsonapi_rpc
from flask_restful import Resource, Api, reqparse, abort
from flask_cors import CORS
from flask import Flask, render_template,request
from flask_socketio import SocketIO,send,emit
import datetime


db = SQLAlchemy()
clients = {}


class Message(SAFRSBase, db.Model):
    __tablename__ = "Message"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String)
    receiver = db.Column(db.String)
    sender = db.Column(db.String)
    send_time = db.Column(db.DateTime)
    is_read = db.Column(db.Boolean)
    
    
    def __str__(self):
        return f'{self.message}'

    @classmethod
    @jsonapi_rpc(http_methods=['GET'])
    def getMessages(cls, *args, **kwargs):
       
        receiver = kwargs['varargs'].split()[0]
        sender = kwargs['varargs'].split()[1]
        list_m = []
        for msg in db.session.query(Message).filter_by(receiver=receiver, sender=sender).all():
            object = {"receiver": msg.receiver, "sender": msg.sender, "is_read": msg.is_read,"send_time": msg.send_time, "text": msg.text}

            #msg.is_read = True
            list_m.append(object)
            socketio.emit('refreshChat')
            db.session.commit()

        for msg in db.session.query(Message).filter_by(receiver=sender, sender=receiver).all():
            object = {"receiver": msg.receiver, "sender": msg.sender, "is_read": msg.is_read,"send_time": msg.send_time, "text": msg.text}
            list_m.append(object)
            db.session.commit()
        sortedMsg = sorted(list_m, key=lambda k: k['send_time'])

        return sortedMsg

    @classmethod
    @jsonapi_rpc(http_methods=['GET'])
    def readMessage(cls, *args, **kwargs):
       
        receiver = kwargs['varargs'].split()[0]
        sender = kwargs['varargs'].split()[1]
        list_m = []
        for msg in db.session.query(Message).filter_by(receiver=receiver, sender=sender).all():
            object = {"receiver": msg.receiver, "sender": msg.sender, "is_read": msg.is_read,"send_time": msg.send_time, "text": msg.text}

            msg.is_read = True
            list_m.append(object)
            socketio.emit('refreshChat')
            db.session.commit()

        for msg in db.session.query(Message).filter_by(receiver=sender, sender=receiver).all():
            object = {"receiver": msg.receiver, "sender": msg.sender, "is_read": msg.is_read,"send_time": msg.send_time, "text": msg.text}
            list_m.append(object)
            db.session.commit()
        sortedMsg = sorted(list_m, key=lambda k: k['send_time'])
        update_mes()

        return sortedMsg


class User(SAFRSBase, db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, index=True)
    password= db.Column(db.String(50))
    online = db.Column(db.Boolean )

    @classmethod
    @jsonapi_rpc(http_methods=['GET'])
    def signUP(cls, *args, **kwargs):
        login = kwargs['varargs'].split()[0]
        password1 = kwargs['varargs'].split()[1]
        user = db.session.query(User).filter_by(name=login).first()
        if user is  None:
            user1 = User(name=login, password=password1, online = False)
            # db.session.add(user1)
            db.session.commit()
            socketio.emit('login')
            update_list()
            return "success"
        return "failed"

    @classmethod
    @jsonapi_rpc(http_methods=['GET'])
    def logIn(cls, *args, **kwargs):
        login = kwargs['varargs'].split()[0]
        password = kwargs['varargs'].split()[1]
        user = db.session.query(User).filter_by(name=login, password=password).first()
        if user is not None:
            user.online = True
            db.session.commit()
            socketio.emit('login')
            update_list()
            return "success"

        return "failed"

    @classmethod
    @jsonapi_rpc(http_methods=['GET'])
    def logOut(cls, *args, **kwargs):

        login = kwargs['varargs']
        user = db.session.query(User).filter_by(name=login).first()
        if user is not None:
            user.online = False
            db.session.commit()
            socketio.emit('login')
            update_list()
            return "success"
        return "failed"

    @classmethod
    @jsonapi_rpc(http_methods=['GET'])
    def sendMessages(cls, *args, **kwargs):
        lista = kwargs['varargs'].split(" ",2)
        sender =lista[0]
        receiver = lista[1]
        messageS = lista[2]
        message = Message( text = messageS, receiver= receiver, sender = sender, send_time =  '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()), is_read = False)
        # db.session.add(message)
        db.session.commit()
        update_mes()
        socketio.emit('refreshM')
        
        return "success"



def create_api(app, HOST="localhost", PORT=5000, API_PREFIX=""):
    api = SAFRSAPI(app, host=HOST, port=PORT, prefix=API_PREFIX)
    #api.expose_object(Server)

    api.expose_object(User)
    api.expose_object(Message)
    print("Created API: http://{}:{}/{}".format(HOST, PORT, API_PREFIX))

def create_app(config_filename=None, host="localhost"):
    app = Flask("demo_app")
    # app.debug=True
    app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///server.sqlite")
    db.init_app(app)

    with app.app_context():
        db.create_all()
        create_api(app, host)
    
    return app
host = "127.0.0.1"
app = create_app(host=host)
socketio = SocketIO(app)
def update_list():
    socketio.emit("update_list",brodcast=True)

def update_mes():
    socketio.emit("update_mes",brodcast=True)


@socketio.on("connect")
def connect():
    print(request.sid," connected")
    # print(active_users)
    # clients[request.sid] = login_queue.pop(0)
    update_list()
@socketio.on("disconnect")
def disconnect():
    print(request.sid," disconnected")
    # active_users.remove(clients[request.sid])
    del clients[request.sid]
    update_list()
if __name__ == "__main__":
    socketio.run(app)




if __name__ == "__main__":
    app.run(host=host)
    socketio.run(app)
 

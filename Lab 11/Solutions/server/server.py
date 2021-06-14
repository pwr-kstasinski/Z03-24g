from flask import Flask,request,jsonify,render_template
from werkzeug.http import HTTP_STATUS_CODES
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_,and_
import datetime
import json
import os
from sys import exit
#import websockets
#import asyncio
#import multiprocessing
from dataclasses import dataclass,asdict
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint
from flask_socketio import send, SocketIO

ser = Flask(__name__)
#ser.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///mudb.sqlite3"
ser.config["SQLALCHEMY_DATABASE_URI"]=os.getenv("DB_CONNECT_STR","sqlite:///mudb.sqlite3")
ser.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True
#ser.config['SECRET_KEY'] = 'secret!'
ser.config['FLASK_ENV'] = 'development'
db = SQLAlchemy(ser)
socketio = SocketIO(ser)
serhost = os.getenv("SERVER_HOST","0.0.0.0")
serport = int(os.getenv("SERVER_PORT","5000"))

def nmessage(fr,to,msg):
    return messages(fr=fr,to=to,msg=msg,sent=datetime.datetime.now(),read=False)
def localserhost():
    return "localhost" if serhost=="0.0.0.0" else serhost

@dataclass
class messages(db.Model):
    _id:int
    fr:str
    to:str
    msg:str
    sent:datetime.datetime
    read:bool
    _id = db.Column("_id",db.Integer,primary_key=True)
    fr = db.Column("fr",db.String(30))
    to = db.Column("to",db.String(30))
    msg = db.Column("msg",db.String(300))
    sent = db.Column("sent",db.DateTime)
    read = db.Column("read",db.Boolean,default=False)

def nuser(login,password):
    return users(login=login,password=password,lastQuery=datetime.datetime.now())

@dataclass
class users(db.Model):
    login = db.Column("id",db.String(30),primary_key=True)
    password = db.Column("password",db.String(30))
    lastQuery = db.Column("lastQuery",db.DateTime)
    active = db.Column("active",db.Boolean,default=False)

def bad_request(message=None,status_code=400):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response

@ser.route("/receive",methods=["GET"])
def download_messages():
    """Endpoint for receiving messages
    ---
    parameters:
      - in: "query"
        name: "id"
        description: "User id"
        required: true
        type: "string"
      - in: "query"
        name: "fr"
        description: "Other user id"
        required: true
        type: "string"
    responses:
        "400":
            description: "Invalid input"
        "200":
            description: "Messages given"
            schema:
                type: "array"
                items:
                    type: "object"
                    properties:
                        _id:
                            type: "int"
                            example: "1"
                        fr:
                            type: "string"
                            example: "you"
                        to:
                            type: "string"
                            example: "me"
                        msg:
                            type: "string"
                            example: "Hello there"
                        read:
                            type: "boolean"
                            example: "true"
                        sent:
                            type: "string"
                            example: "123132"
    """
    data = request.args
    if "id" not in data:
        return bad_request("Necessary parameter id not given")
    if "fr" not in data:
        return bad_request("Necessary parameter id not given")
    uid = data["id"]
    if uid == "":
        result = messages.query.filter(messages.to=="")
    else:
        user = users.query.filter_by(login=uid).first()
        if not user:
            return bad_request("ID not registered")
        user.lastQuery = datetime.datetime.now()
        result = messages.query.filter(or_(and_(messages.to==uid,messages.fr==data["fr"]),and_(messages.to==data["fr"],messages.fr==uid)))
    list = [asdict(x) for x in result.order_by(messages.sent).all()]
    db.session.commit()
    return jsonify(list)

@ser.route("/send",methods=["POST"])
def accept_message():
    """Endpoint for sending messages
    ---
    parameters:
      - in: "body"
        name: "message"
        description: "Message definition"
        required: true
        schema:
            type: "object"
            properties:
                fr:
                    type: "string"
                    example: "you"
                to:
                    type: "string"
                    example: "me"
                msg:
                    type: "string"
                    example: "Hello there"
    responses:
        "400":
            description: "Invalid input"
        "200":
            description: "Message sent"
    """
    data = request.get_json() or {}
    print(data)
    if "fr" not in data or "to" not in data or "msg" not in data:
        return bad_request("Any of necessary parameters from/to/message not found")
    user = users.query.filter_by(login=data["fr"]).first()
    if not user:
        return bad_request("Sender's ID not registered")
    user.lastQuery = datetime.datetime.now()
    if not data["to"]:
        db.session.add(nmessage(data["fr"],data["to"],data["msg"]))
    else:
        user = users.query.filter_by(login=data["to"]).first()
        if not user:
            return bad_request("Receiver's ID not registered")
        db.session.add(nmessage(data["fr"],data["to"],data["msg"]))
    db.session.commit()
    socketio.emit('any',json.dumps({"code":"msgrec","to":data["to"],"fr":data["fr"]}))
    return "OK"

@ser.route("/register",methods=["POST"])
def register_user():
    """Endpoint for registering users
    ---
    parameters:
      - in: "query"
        name: "id"
        description: "User id"
        required: true
        type: "string"
      - in: "query"
        name: "pass"
        description: "User password"
        required: true
        type: "string"
    responses:
        "400":
            description: "Invalid input"
        "200":
            description: "Succesfully registered"
    """
    data = request.args
    if "id" not in data:
        return bad_request("Necessary parameter id not given")
    if "pass" not in data:
        return bad_request("Necessary parameter pass not given")
    uid = data["id"]
    if uid == "ALL":
        return bad_request("Forbidden ID")
    user = users.query.filter_by(login=uid).first()
    if user:
        return bad_request("ID already registered")
    usr = nuser(data["id"],data["pass"])
    db.session.add(usr)
    db.session.commit()
    socketio.emit('any',json.dumps({"code":"usrreg","uid":uid}))
    return "OK"

@ser.route("/login",methods=["GET"])
def login_user():
    """Endpoint for logging users
    ---
    parameters:
      - in: "query"
        name: "id"
        description: "User id"
        required: true
        type: "string"
      - in: "query"
        name: "pass"
        description: "User password"
        required: true
        type: "string"
    responses:
        "400":
            description: "Invalid input"
        "200":
            description: "Succesfully logged in"
    """
    data = request.args
    if "id" not in data:
        return bad_request("Necessary parameter id not given")
    if "pass" not in data:
        return bad_request("Necessary parameter pass not given")
    uid = data["id"]
    passw = data["pass"]
    user = users.query.filter_by(login=uid,password=passw).first()
    if not user:
        return bad_request("ID or password wrong")
    user.lastQuery = datetime.datetime.now()
    user.active = True
    db.session.commit()
    socketio.emit('any',json.dumps({"code":"usrlog","uid":uid}))
    return "OK"

@ser.route("/logout",methods=["GET"])
def logout_user():
    """Endpoint for user logout
    ---
    parameters:
      - in: "query"
        name: "id"
        description: "User id"
        required: true
        type: "string"
    responses:
        "400":
            description: "Invalid input"
        "200":
            description: "Succesfully logged out"
    """
    data = request.args
    if "id" not in data:
        return bad_request("Necessary parameter id not given")
    uid = data["id"]
    user = users.query.filter_by(login=uid).first()
    if not user:
        return bad_request("Wrong ID")
    user.active = False
    db.session.commit()
    socketio.emit('any',json.dumps({"code":"usrlog","uid":uid}))
    return "OK"

@ser.route("/logged",methods=["GET"])
def get_active_users():
    """Endpoint for getting active users
    ---
    responses:
        "200":
            description: "Succesfully obtained logged users"
            schema:
                type: "array"
                items:
                    type: "string"
                    example: "thatsme"
    """
    timeTreshold = datetime.datetime.now() - datetime.timedelta(seconds=5)
    ausrs = users.query.filter(users.active==True).all()
    return jsonify([u.login for u in ausrs])

@ser.route("/users",methods=["GET"])
def get_users():
    """Endpoint for getting all users
    ---
    parameters:
      - in: "query"
        name: "id"
        description: "User id"
        required: true
        type: "string"
    responses:
        "200":
            description: "Succesfully parsed request"
            schema:
                type: "array"
                items:
                    type: "object"
                    properties:
                        uid:
                            type: "string"
                            example: "him"
                        active:
                            type: "boolean"
                            example: "false"
                        last:
                            type: "string"
                            example: "123123"
    """
    data = request.args
    if "id" not in data:
        return bad_request("Necessary parameter id not given")
    timeTreshold = datetime.datetime.now() - datetime.timedelta(seconds=5)
    ausrs = users.query.all()
    def queryForLastMsg(fr,to):
        f = messages.query.filter(messages.fr==fr,messages.to==to).order_by(messages.sent.desc()).first()
        t = messages.query.filter(messages.fr==to,messages.to==fr).order_by(messages.sent.desc()).first()
        if not f:
            return t.sent if t else datetime.datetime.min
        if not t:
            return f.sent if f else datetime.datetime.min
        return f.sent if f.sent>t.sent else t.sent
    return jsonify([{"uid":u.login,"active":u.active,"last":queryForLastMsg(u.login,data["id"])} for u in ausrs])

@ser.route("/read",methods=["PUT"])
def mark_message_read():
    """Endpoint for marking messages as read
    ---
    parameters:
      - in: "query"
        name: "id"
        description: "Id of message to mark as read"
        required: true
        type: "int"
    responses:
        "400":
            description: "Invalid input"
        "200":
            description: "Succesfully marked as read"
    """
    
    data = request.args
    if "id" not in data:
        return bad_request("Necessary parameter id not given")
    msg = messages.query.filter_by(_id=data["id"]).first()
    msg.read = True
    socketio.emit('any',json.dumps({"code":"usrlog","fr":msg.fr,"to":msg.to,"id":msg._id}))
    db.session.commit()
    return "OK"

@ser.route("/unread",methods=["GET"])
def get_unread_messages_count():
    """Endpoint for getting active users
    ---
    parameters:
      - in: "query"
        name: "fr"
        description: "Id of user who sent messages"
        required: true
        type: "string"
      - in: "query"
        name: "id"
        description: "Current user id"
        required: true
        type: "string"
    responses:
        "200":
            description: "Number of unread messages in that conversation"
            schema:
                type: "int"
                example: "10"
    """
    data = request.args
    if "id" not in data:
        return bad_request("Necessary parameter id not given")
    if "fr" not in data:
        return bad_request("Necessary parameter fr not given")
    uid=data["id"]
    if not uid:
        result = messages.query.filter(messages.to=="",messages.fr!=data["fr"],messages.read==False)
    else:
        user = users.query.filter_by(login=data["id"]).first()
        if not user:
            return bad_request("ID not registered")
        result = messages.query.filter_by(to=uid,fr=data["fr"],read=False)
        user.lastQuery = datetime.datetime.now()
    ct = result.count()
    return str(ct) if ct else "0"

@ser.route("/api",methods=["GET"])
def render_api():
    swag = swagger(ser)
    swag['host'] = "{}:{}".format(localserhost(),serport)
    return jsonify(swag)

@ser.route("/")
def index():
    return render_template('index.html', title="page")

@ser.route("/healthcheck")
def healthcheck():
    """Endpoint for healthchecks
    ---
    responses:
        "200":
            description: "I'm fine, thanks"
            schema:
                type: "str"
                example: "I'm fine, thanks"
    """
    return "I'm fine, thanks"

@ser.route("/fail")
def fail():
    """Endpoint for making the server shut down. You monster.
    ---
    responses:
        "500":
            description: "Exited, thus no further response"
    """
    exit(0)

swaggerui_blueprint = get_swaggerui_blueprint(
    "/docs",
    "http://{}:{}/api".format(localserhost(),serport)
)

def runFlask():
    db.create_all()
    ser.register_blueprint(swaggerui_blueprint)
    #print(os.getenv('DB_CONNECT_STR','nope'))
    #ser.run(debug=True, host='0.0.0.0')
    print("fun")
    socketio.run(ser,debug=True, host=serhost, port=serport)
    #print("hello")

if __name__ == "__main__":
    runFlask()
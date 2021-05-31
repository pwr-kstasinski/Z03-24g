from flask import Flask,request,jsonify,render_template
from werkzeug.http import HTTP_STATUS_CODES
from flask_sqlalchemy import SQLAlchemy
import datetime
import json
import websockets
import asyncio
import multiprocessing
from dataclasses import dataclass
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint

ser = Flask(__name__)
ser.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///mudb.sqlite3"
ser.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True
db = SQLAlchemy(ser)
wsbuffer = []

def nmessage(fr,to,msg):
    return messages(fr=fr,to=to,msg=msg)

def sendToWS(data):
    wsbuffer.append(data)

async def wsLoop(websocket, path):
    while wsbuffer:
        cd = wsbuffer.pop(0)
        await websocket.send(cd)

@dataclass
class messages(db.Model):
    id:int
    fr:str
    to:str
    msg:str
    sent:datetime.datetime
    read:bool
    id = db.Column("id",db.Integer,primary_key=True)
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
                        fr:
                            type: "string"
                            example: "you"
                        to:
                            type: "string"
                            example: "me"
                        msg:
                            type: "string"
                            example: "Hello there"
    """
    data = request.args
    if "id" not in data:
        return bad_request("Necessary parameter id not given")
    uid = data["id"]
    user = users.query.filter_by(login=uid).first()
    if not user:
        return bad_request("ID not registered")
    result = messages.query.filter_by(to=uid)
    user.lastQuery = datetime.datetime.now()
    json = jsonify(result.all())
    result.delete()
    db.session.commit()
    return json

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
        for x in users.query.all():
            if x.login != data["fr"]:
                db.session.add(nmessage(data["fr"],x.login,data["msg"]))
    else:
        user = users.query.filter_by(login=data["to"]).first()
        if not user:
            return bad_request("Receiver's ID not registered")
        db.session.add(nmessage(data["fr"],data["to"],data["msg"]))
    db.session.commit()
    sendToWS({"code":"msgrec","to":data["to"]})
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
    user = users.query.filter_by(login=uid).first()
    if user:
        return bad_request("ID already registered")
    usr = nuser(data["id"],data["pass"])
    db.session.add(usr)
    db.session.commit()
    sendToWS({"code":"usrreg","uid":uid})
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
    sendToWS({"code":"usrlog","uid":uid})
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
    user.active = True
    db.session.commit()
    sendToWS({"code":"usrlog","uid":uid})
    return "OK"

@ser.route("/logged",methods=["GET"])
def get_active_users():
    """Endpoint for getting active users
    ---
    responses:
        "200":
            description: "Succesfully logged in"
            schema:
                type: "array"
                items:
                    type: "string"
                    example: "thatsme"
    """
    timeTreshold = datetime.datetime.now() - datetime.timedelta(seconds=5)
    ausrs = users.query.filter(users.active==True).all()
    return jsonify([u.login for u in ausrs])

@ser.route("/read",methods=["PUT"])
def mark_message_read():
    """Endpoint for marking messages as read
    ---
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
    msg = messages.query.filter_by(id=data["id"]).first()
    msg.read = True
    return "OK"

@ser.route("/unread",methods=["GET"])
def get_unread_messages_count():
    """Endpoint for getting active users
    ---
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
    user = users.query.filter_by(login=data["id"]).first()
    if not user:
        return bad_request("ID not registered")
    result = messages.query.filter_by(to=uid,fr=data["fr"])
    user.lastQuery = datetime.datetime.now()
    return result.count()

@ser.route("/api",methods=["GET"])
def render_api():
    swag = swagger(ser)
    swag['host'] = "localhost:5000"
    return jsonify(swag)

swaggerui_blueprint = get_swaggerui_blueprint(
    "/docs",
    "http://localhost:5000/api"
)

async def respond(websocket, path):
    while True:
        message = json.dumps({"code":"usrlog","uid":"arg"})
        await websocket.send(message)
        await asyncio.sleep(3)

def runFlask():
    db.create_all()
    ser.register_blueprint(swaggerui_blueprint)
    ser.run(debug=True, host="localhost")

def runWebsockets():
    try:
        start_server = websockets.serve(respond, "localhost", 6000)
    finally:
        pass
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    p_flask = multiprocessing.Process(target=runFlask)
    p_ws = multiprocessing.Process(target=runWebsockets)
    p_flask.start()
    p_ws.start()
    p_flask.join()
    p_ws.join()
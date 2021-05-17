from flask import Flask,request,jsonify,render_template
from werkzeug.http import HTTP_STATUS_CODES
from flask_sqlalchemy import SQLAlchemy
import datetime

ser = Flask(__name__)
ser.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///mudb.sqlite3"
db = SQLAlchemy(ser)
messageID = 0

def getNextMessageID():
    messageID+=1
    return messageID

class messages(db.Model):
    id = db.Column("id",db.Integer,primary_key=True)
    fr = db.Column("from",db.String(30))
    to = db.Column("to",db.String(30))
    msg = db.Column("message",db.String(300))
    def __init__(self,fr,to,msg):
        self.id = getNextMessageID()
        self.fr = fr
        self.to = to
        self.msg = msg
        
class users(db.Model):
    login = db.Column("id",db.String(30),primary_key=True)
    password = db.Column("password",db.String(30))
    lastQuery = db.Column("lastQuery",db.DateTime)
    def __init__(self,login,password):
        self.login = login
        self.password = password
        self.lastQuery = datetime.datetime.now()

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
                        from:
                            type: "string"
                            example: "you"
                        to:
                            type: "string"
                            example: "me"
                        message:
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
    json = jsonify(result)
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
                from:
                    type: "string"
                    example: "you"
                to:
                    type: "string"
                    example: "me"
                message:
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
    if "from" not in data or "to" not in data or "message" not in data:
        return bad_request("Any of necessary parameters from/to/message not found")
    user = users.query.filter_by(login=data["to"]).first()
    if not user:
        return bad_request("Receiver's ID not registered")
    user = users.query.filter_by(login=data["from"]).first()
    if not user:
        return bad_request("Sender's ID not registered")
    user.lastQuery = datetime.datetime.now()
    db.session.add(messages(data["from"],data["to"],data["message"]))###
    db.session.commit()
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
    usr = users(data["id"],data["password"])
    db.session.add(usr)
    db.session.commit()
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
    db.session.commit()
    return "OK"

@ser.route("/logged",methods=["GET"])
def get_active_users():
    """Endpoint for getting active users
    ---
    responses:
        "200":
            description: "Succesfully logged in"
    """
    timeTreshold = datetime.datetime.now() - datetime.timedelta(seconds=5)
    ausrs = users.query.filter(users.lastQuery>timeTreshold)
    return "OK"

@ser.route("/api",methods=["GET"])
def render_api():
    return render_template("index.html")

if __name__ == "__main__":
    db.create_all()
    ser.run(debug=True, host="0.0.0.0")
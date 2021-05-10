from flask import Flask,request,jsonify
from werkzeug.http import HTTP_STATUS_CODES

ser = Flask(__name__)
messages = []
users = []

def message_from_json(data):
    return Message(data['from'],data['to'],data['message'])

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
    global messages
    data = request.args
    if "id" not in data:
        return bad_request("Necessary parameter id not given")
    uid = data["id"]
    if uid not in users:
        return bad_request("ID not registered")
    result, rest = [], []
    for x in messages:
        (result, rest)[x["to"]==uid].append(x)
    messages = rest
    return jsonify(result)

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
    if data["from"] not in users:
        return bad_request("Sender's ID not registered")
    if data["to"] not in users:
        return bad_request("Receiver's ID not registered")
    messages.append({"from":data["from"],"to":data["to"],"message":data["message"]})
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
    if data["id"] in users:
        return bad_request("ID already registered")
    users.append(data["id"])
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
    if data["id"] not in users:
        return bad_request("ID not registered")
    return "OK"

if __name__ == "__main__":
    ser.run(debug=True, host="0.0.0.0")
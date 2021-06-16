import json
import os
from flask import Flask, request, jsonify
from werkzeug.http import HTTP_STATUS_CODES
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_swagger_ui import get_swaggerui_blueprint
from flask_marshmallow import Marshmallow
from flask_socketio import SocketIO
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{os.environ["DB_USER"]}:{os.environ["DB_PASS"]}@{os.environ["DB_HOST"]}/{os.environ["DB_NAME"]}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
socketio = SocketIO(app)


SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL)


class Message(db.Model):
    __tablename__ = 'Messages'
    id = db.Column(db.Integer, primary_key=True)
    receiver_id = db.Column(db.Integer)
    sender_id = db.Column(db.Integer)
    message = db.Column(db.String)
    date = db.Column(db.DateTime)
    read = db.Column(db.Boolean, default=False)


class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    logged = db.Column(db.Boolean, default=False)


class UserSchema(ma.Schema):
    class Meta:
        model = User
        fields = ('logged', 'username', 'id')


class MessageSchema(ma.Schema):
    class Meta:
        model = Message
        fields = ('message', 'date', 'sender_id', 'receiver_id', 'read')


def invalid_request(message=None, status_code=400):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response


@app.route('/download', methods=['GET'])
def download_messages():
    data = request.args
    if 'user_id' not in data or 'partner_id' not in data:
        return invalid_request('Necessary parameters not given')
    user = db.session.query(User).filter_by(id=data['partner_id']).first()
    user2 = db.session.query(User).filter_by(id=data['user_id']).first()
    partner_id: int = int(data['partner_id'])
    if partner_id == 0:
        messages = db.session.query(Message).filter((Message.receiver_id == data['partner_id']))
        message_schema = MessageSchema(many=True)
        result = message_schema.dump(messages)
        return jsonify(result)
    elif user is None or user2 is None:
        return invalid_request('One of the users doesnt exist')

    messages = db.session.query(Message).filter(((Message.sender_id == data['user_id']) &
                                     (Message.receiver_id == data['partner_id'])) |
                                    ((Message.sender_id == data['partner_id']) &
                                     (Message.receiver_id == data['user_id']))
                                    ).order_by(Message.date).all()
    message_schema = MessageSchema(many=True)
    result = message_schema.dump(messages)
    return jsonify(result)


@app.route('/send', methods=['POST'])
def send_message():
    data = request.get_json() or {}
    if 'sender_id' not in data or 'receiver_id' not in data or 'message' not in data or 'date' not in data:
        return invalid_request('Any of necessary parameters not found')
    message = Message(receiver_id=data['receiver_id'], sender_id=data['sender_id'], message=data['message'],
                      date=datetime.datetime.strptime(data['date'], "%m/%d/%Y, %H:%M:%S"))
    db.session.add(message)
    db.session.commit()
    socketio.emit('all', json.dumps({'action': 'message',
                                     'sender_id': data['sender_id'],
                                     'receiver_id': data['receiver_id'],
                                     'message': data['message'],
                                     'date': data['date']}))
    return 'OK'


@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json() or {}
    if 'username' not in data or 'password' not in data:
        return invalid_request('Necessary parameters not given')
    user = db.session.query(User).filter_by(username=data['username']).first()
    if user is not None:
        return invalid_request('User already exists')
    else:
        user = User(username=data['username'], password=data['password'])
        db.session.add(user)
        db.session.commit()
    socketio.emit('all', json.dumps({'action': 'user_refresh'}))
    return 'OK'


@app.route('/login', methods=['GET'])
def login_user():
    data = request.args
    if 'username' not in data or 'password' not in data:
        return invalid_request('Necessary parameters not given')
    user = db.session.query(User).filter_by(username=data['username'], password=data['password']).first()
    if user is None:
        return invalid_request('Wrong password or username')
    user.logged = True
    db.session.commit()
    socketio.emit('all', json.dumps({'action': 'user_refresh'}))
    return 'OK'


@app.route('/logout', methods=['GET'])
def logout_user():
    data = request.args
    if 'username' not in data:
        return invalid_request('Necessary parameters not given')
    user = db.session.query(User).filter_by(username=data['username']).first()
    if user is None:
        return invalid_request('Wrong username')
    user.logged = False
    db.session.commit()
    socketio.emit('all', json.dumps({'action': 'user_refresh'}))
    return 'OK'


@app.route('/users', methods=['GET'])
def get_logged_users():
    user_id = request.args
    if 'id' not in user_id:
        return invalid_request('Necessary parameters not given')
    user_id = int(user_id['id'])
    users = db.session.query(User).order_by(User.logged.desc()).all()
    user_schema = UserSchema(many=True)
    output = user_schema.dump(users)
    for user in output:
        last_message = db.session.query(Message).filter(((Message.sender_id == user_id) &
                                             (Message.receiver_id == user['id'])) |
                                            ((Message.sender_id == user['id']) &
                                             (Message.receiver_id == user_id))
                                            ).order_by(Message.date.desc()).first()
        count = db.session.query(Message).filter((Message.sender_id == user['id']) & (Message.receiver_id == user_id) &
                                     (Message.read == False)).count()
        message_schema = MessageSchema()
        result = message_schema.dump(last_message)
        user['unread'] = count
        if result == {}:
            user['last'] = ""
        else:
            user['last'] = result['date']
        general = db.session.query(Message).filter((Message.receiver_id == 0) &
                                     (Message.read == False)).count()
        gen = {
            'id': 0,
            'username': '#General',
            'logged': True,
            'unread': general,
            'last': ""
        }

    output.sort(key=lambda k: k['last'], reverse=True)
    output.append(gen)
    return jsonify(output)


@app.route('/read', methods=['GET'])
def mark_as_read():
    data = request.args
    if 'user_id' not in data or 'partner_id' not in data:
        return invalid_request('Necessary parameters not given')
    if data['partner_id'] == '0':
        messages = db.session.query(Message).filter(Message.receiver_id == data['partner_id']).all()
        for m in messages:
            m.read = True
            db.session.commit()
    else:
        messages = db.session.query(Message).filter(
            (Message.sender_id == data['partner_id']) & (Message.receiver_id == data['user_id'])).all()
        for m in messages:
            m.read = True
            db.session.commit()
    socketio.emit('all', json.dumps({'action': 'read',
                                     'sender_id': data['partner_id'],
                                     'receiver_id': data['user_id']}))

    return 'OK'


@app.route('/user', methods=['GET'])
def get_user():
    data = request.args
    if 'username' not in data:
        return invalid_request('Necessary parameters not given')
    user = db.session.query(User).filter_by(username=data['username']).first()
    if user is None:
        return invalid_request('Wrong username')
    output = {
        'id': user.id,
        'username': user.username,
        'logged': user.logged,
        'unread': 0,
        'last': ""
    }
    return jsonify(output)

Healthy = True

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    global Healthy
    if Healthy:
        return(invalid_request(message='OK, i am good', status_code=200))
    return(invalid_request(message='Server is in a bad condition', status_code=500))

@app.route('/makesick', methods=['GET'])
def makesick():
    global Healthy
    Healthy = False
    return(invalid_request('Made me sick', 200))

app.register_blueprint(swaggerui_blueprint)
print('dziala')
socketio.run(app, host='0.0.0.0', port=5000)

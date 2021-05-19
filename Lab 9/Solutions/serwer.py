from flask import Flask, request, jsonify
from werkzeug.http import HTTP_STATUS_CODES
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_swagger_ui import get_swaggerui_blueprint
from flask_marshmallow import Marshmallow

app = Flask(__name__)
db = SQLAlchemy(app)
ma = Marshmallow(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databasee.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger12.json'
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
        fields = ('message', 'date', 'sender_id', 'receiver_id')


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
    print(data)
    if 'user_id' not in data or 'partner_id' not in data:
        return invalid_request('Necessary parameters not given')
    user = db.session.query(User).filter_by(id=data['partner_id']).first()
    user2 = db.session.query(User).filter_by(id=data['user_id']).first()
    if user is None or user2 is None:
        return invalid_request('One of the users doesnt exist')
    messages = Message.query.filter(((Message.sender_id == data['user_id']) &
                                    (Message.receiver_id == data['partner_id'])) |
                                    ((Message.sender_id == data['partner_id']) &
                                     (Message.receiver_id == data['user_id']))
                                    ).order_by(Message.date).all()
    message_schema = MessageSchema(many=True)
    result = message_schema.dump(messages)
    print(messages)
    print(result)
    return jsonify(result)


@app.route('/send', methods=['POST'])
def send_message():
    data = request.get_json() or {}
    print(data)
    if 'sender_id' not in data or 'receiver_id' not in data or 'message' not in data or 'date' not in data:
        return invalid_request('Any of necessary parameters not found')
    message = Message(receiver_id=data['receiver_id'], sender_id=data['sender_id'], message=data['message'],
                      date=datetime.datetime.strptime(data['date'], "%m/%d/%Y, %H:%M:%S"))
    db.session.add(message)
    db.session.commit()
    return 'OK'


@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json() or {}
    if 'username' not in data or 'password' not in data:
        return invalid_request('Necessary parameters not given')
    user = User.query.filter_by(username=data['username']).first()
    if user is not None:
        return invalid_request('User already exists')
    else:
        user = User(username=data['username'], password=data['password'])
        db.session.add(user)
        db.session.commit()
    return 'OK'


@app.route('/login', methods=['GET'])
def login_user():
    data = request.args
    if 'username' not in data or 'password' not in data:
        return invalid_request('Necessary parameters not given')
    user = User.query.filter_by(username=data['username'], password=data['password']).first()
    if user is None:
        return invalid_request('Wrong password or username')
    user.logged = True
    db.session.commit()
    return 'OK'


@app.route('/logout', methods=['GET'])
def logout_user():
    data = request.args
    if 'username' not in data:
        return invalid_request('Necessary parameters not given')
    user = User.query.filter_by(username=data['username']).first()
    if user is None:
        return invalid_request('Wrong username')
    user.logged = False
    db.session.commit()
    return 'OK'


@app.route('/users', methods=['GET'])
def get_logged_users():
    user = User.query.all()
    user_schema = UserSchema(many=True)
    output = user_schema.dump(user)
    print(output)
    return jsonify(output)


if __name__ == '__main__':
    app.register_blueprint(swaggerui_blueprint)
    app.run(host='localhost')

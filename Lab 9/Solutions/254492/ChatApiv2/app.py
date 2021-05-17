from operator import add
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import pickle
import ast
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from sqlalchemy import or_

import sqlalchemy

app = Flask(__name__)
api = Api(app)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
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

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content

class GeneralMessages (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(2000), nullable=False)

    def __init__(self, sender, content):
        self.sender = sender
        self.content = content


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
        fields = ('sender', 'receiver', 'content')

message_schema = MessageSchema(many=True)



'''
users - { user1: [], user2: []}
{sender: nickname, content: message}

'''

with open('users.pickle', 'rb') as handle:
    users = pickle.load(handle)


def custom_ret_json(message="All OK", code=200, contents=None):
    return {"code": code, "message": message, "contents": contents}, code


def parse_request_args(args):
    print(args)
    if "sender" not in args:
        return custom_ret_json("sender is required", 400)
    if "content" not in args or not args.get("content"):
        return custom_ret_json("message contents are required", 400)
    return False

def serialize():
    with open('users.pickle', 'wb') as handling:
        pickle.dump(users, handling, protocol=pickle.HIGHEST_PROTOCOL)

class GeneralMessage(Resource):
    def get(self, password):
        messages = message_schema.dump(GeneralMessages.query.all())
        return custom_ret_json(contents=messages)

    def post(self, password):
        message = ast.literal_eval(request.data.decode())
        error = parse_request_args(message)
        if error:
            return error
        sender_user = users_schema_pass.dump(Users.query.filter_by(username=message['sender']))
        if (not sender_user):
            return custom_ret_json("Username not found", 404)
        if(sender_user[0]['password'] == password):
            db.session.add(GeneralMessages(message['sender'], message['content']))
            db.session.commit()
            print(message_schema.dump(GeneralMessages.query.all()))
            return custom_ret_json()
        return custom_ret_json("Wrong password", 401)


class Message(Resource):
    def get(self, login, password):
        user = users_schema_pass.dump(Users.query.filter_by(username=login))
        if(not user):
            return custom_ret_json("Username not found", 404)
        if(user[0]['password'] == password):
            messages = message_schema.dump(Messages.query.filter(or_(Messages.receiver==login, (Messages.sender==login))))
            return custom_ret_json(contents=messages)
        return custom_ret_json('Wrong password', 401)

    def post(self, login, password):
        # if login not in users:
        #     return custom_ret_json("Username not found", 404)
        # error = parse_request_args(ast.literal_eval(request.data.decode()))
        # if error:
        #     return error
        # users[login].append(ast.literal_eval(request.data.decode()))
        # serialize()
        # print(request.data)
        # print(request.data.decode())
        # print(ast.literal_eval(request.data.decode()))
        # return custom_ret_json()
        user = users_schema_pass.dump(Users.query.filter_by(username=login))
        if(user):
            message = ast.literal_eval(request.data.decode())
            error = parse_request_args(message)
            if error:
                return error
            sender_user = users_schema_pass.dump(Users.query.filter_by(username=message['sender']))
            if (not sender_user):
                return custom_ret_json("Username not found", 404)
            if(sender_user[0]['password'] == password):
                db.session.add(Messages(message['sender'], login, message['content']))
                db.session.commit()
                print(message_schema.dump(Messages.query.all()))
                return custom_ret_json()
            return custom_ret_json("Wrong password", 401)

        return custom_ret_json("Username not found", 404)


class Login(Resource):
    def get(self, login, password):
        user = users_schema_pass.dump(Users.query.filter_by(username=login))
        if(not user):
            return custom_ret_json("Username not found", 404)
        if(user[0]['password'] == password):
            Users.query.filter_by(username=login).update({Users.online: True}, synchronize_session=False)
            db.session.commit()
            return custom_ret_json()
        return custom_ret_json('Wrong password', 401)


class Logout(Resource):
    def get(self, login, password):
        user = users_schema_pass.dump(Users.query.filter_by(username=login))
        if(not user):
            return custom_ret_json("Username not found", 404)
        if(user[0]['password'] == password):
            Users.query.filter_by(username=login).update({Users.online: False}, synchronize_session=False)
            db.session.commit()
            return custom_ret_json()
        return custom_ret_json('Wrong password', 401)




class User(Resource):
    def get(self, login, password):
        user = users_schema_pass.dump(Users.query.filter_by(username=login))
        if(not user):
            return custom_ret_json("Username not found", 404)
        if(user[0]['password'] == password):

            return custom_ret_json(contents=users_schema.dump(Users.query.all()))
        
        return custom_ret_json('Wrong password', 401)

    def post(self, login, password):
        try:
            db.session.add(Users(login, password))
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            return custom_ret_json("Username already exists", 409)
        return custom_ret_json()

    def delete(self, login, password):
        user = users_schema_pass.dump(Users.query.filter_by(username=login))
        if(not user):
            return custom_ret_json("Username not found", 404)
        if(user[0]['password'] == password):
            Users.query.filter_by(username=login).delete()
            print(users_schema_pass.dump(Users.query.all()))
            db.session.commit()
            return custom_ret_json()
        
        return custom_ret_json('Wrong password', 401)


api.add_resource(User, "/users/<string:login>/<string:password>")
api.add_resource(Message, "/messagePanel/<string:login>/<string:password>")
api.add_resource(GeneralMessage, "/messagePanel/general/<string:password>")
api.add_resource(Login, "/login/<string:login>/<string:password>")
api.add_resource(Logout, "/logout/<string:login>/<string:password>")

app.config["CACHE TYPE"] = "null"

CORS(app)

if __name__ == '__main__':
    app.run(debug=True)

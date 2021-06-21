from flask import Flask, request
from flask_restful import Api, Resource
import pickle
import ast
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)

'''
users - { user1: [], user2: []}
{sender: nickname, content: message}

'''

with open('users.pickle', 'rb') as handle:
    users = pickle.load(handle)


def custom_ret_json(message="All OK", code=200, contents=None):
    return {"code": code, "message": message, "contents": contents}, code


def non_empty_string(s):
    if not s:
        raise ValueError("Must not be empty string")
    return s


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


class Message(Resource):
    def get(self, login):
        if login not in users:
            return custom_ret_json("Username not found", 404)
        ret_queue = users[login]
        users[login] = users[login][len(ret_queue):]
        serialize()
        return custom_ret_json(contents=ret_queue)

    def post(self, login):
        if login not in users:
            return custom_ret_json("Username not found", 404)
        error = parse_request_args(ast.literal_eval(request.data.decode()))
        if error:
            return error
        users[login].append(ast.literal_eval(request.data.decode()))
        serialize()
        print(request.data)
        print(request.data.decode())
        print(ast.literal_eval(request.data.decode()))
        return custom_ret_json()


class Login(Resource):
    def get(self, login):
        if login not in users:
            return custom_ret_json("Username not found", 404)
        return custom_ret_json()


class User(Resource):
    def get(self, login):
        if login not in users:
            return custom_ret_json("Username not found", 404)
        return custom_ret_json(contents=[user for user in users if user != login])

    def post(self, login):
        if login in users:
            return custom_ret_json("Username already exists", 409)
        users[login] = []
        serialize()
        return custom_ret_json()

    def delete(self, login):
        if login not in users:
            return custom_ret_json("Username not found", 404)
        del users[login]
        serialize()
        return custom_ret_json()


api.add_resource(User, "/users/<string:login>")
api.add_resource(Message, "/messagePanel/<string:login>")
api.add_resource(Login, "/login/<string:login>")
app.config["CACHE TYPE"] ="null"
CORS(app)
if __name__ == '__main__':
    app.run(debug=True)

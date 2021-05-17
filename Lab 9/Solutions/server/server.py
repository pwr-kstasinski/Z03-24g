import datetime
from http import HTTPStatus
from typing import Tuple

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy

import safrs

db = SQLAlchemy()
auth = HTTPBasicAuth()

ID_COLUMN_TYPE = db.String(36)


@auth.verify_password
def verify_password(username_or_token, password):
    if request.method == "POST" and request.url_rule.rule == "/Users/":
        return True
    query = User.query.filter_by(name=username_or_token, _password=password)
    user: User = query.first()
    if user is None:
        return False

    user.last_active = datetime.datetime.now()
    if request.url_rule.rule == '/Users/<string:UserId>/incoming_messages' and request.view_args["UserId"] != user.id:
        return False
    return True


class User(safrs.SAFRSBase, db.Model):
    """
        description: User description
    """
    __tablename__ = 'Users'
    http_methods = ["get", "post", "delete"]
    custom_decorators = [auth.login_required]

    id = db.Column(ID_COLUMN_TYPE, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    _password = db.Column(db.String(30))
    last_active = db.Column(db.DateTime)

    incoming_messages = db.relationship("Message", back_populates="to_user")
    incoming_messages.http_methods = ["get"]

    @safrs.jsonapi_attr
    def password(self):
        """---
            "_password" is hidden because of the "_" prefix, provide a custom attribute "password" the Person fields
        """
        return "hidden"

    @password.setter
    def password(self, val):
        """
            Allow setting _password
        """
        self._password = val


class Message(safrs.SAFRSBase, db.Model):
    """
        description: User description
    """
    __tablename__ = 'Messages'
    http_methods = ["get", "post", "delete"]
    exclude_attrs = ["to_user"]
    id = db.Column(ID_COLUMN_TYPE, primary_key=True)
    content = db.Column(db.String(300))
    from_user_id = db.Column(ID_COLUMN_TYPE)
    to_user_id = db.Column(ID_COLUMN_TYPE, db.ForeignKey("Users.id"))
    to_user = db.relationship("User", back_populates="incoming_messages")
    custom_decorators = [auth.login_required]


HOST = "localhost"
PORT = 5000
app = Flask("Messages server")
username = "root"
password = "my-secret-pw"
server = "localhost"
db_name = "messages"
db_uri = f"mysql+mysqlconnector://{username}:{password}@{server}/{db_name}"
app.config.update(SQLALCHEMY_DATABASE_URI=db_uri, DEBUG=True)
db.init_app(app)
db.app = app
db.create_all()
API_PREFIX = ""
with app.app_context():
    custom_swagger = {
        "securityDefinitions": {
            "BasicAuth": {"type": "basic"}
        },
        "security": [{"BasicAuth": []}],
    }

    api = safrs.SAFRSAPI(
        app,
        host=HOST,
        port=PORT,
        prefix=API_PREFIX,
        custom_swagger=custom_swagger
    )

    api.expose_object(User)
    api.expose_object(Message)

    print("Starting API: http://{}:{}{}".format(HOST, PORT, API_PREFIX))
    app.run(host=HOST, port=PORT)

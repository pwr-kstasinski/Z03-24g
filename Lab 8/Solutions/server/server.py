import json
from http import HTTPStatus

import safrs.response
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from safrs import SAFRSBase, SAFRSAPI, jsonapi_rpc, jsonapi
from safrs.base import Included

db = SQLAlchemy()


class User(SAFRSBase, db.Model):
    """
        description: User description
    """
    __tablename__ = 'Users'
    http_methods = ["get", "post", "delete"]
    # exclude_attrs = ["password"]
    id = db.Column(db.String, primary_key=True)
    incoming_messages = db.relationship("Message", back_populates="to_user")
    incoming_messages.http_methods = ["get"]
    name = db.Column(db.String)
    password = db.Column(db.String)

    @classmethod
    @jsonapi_rpc(http_methods=["POST"])
    def login(cls, *args, **kwargs):
        from safrs.jsonapi import make_response
        """
            description : login user
            summary: login user
            args:
                name:
                    type : string
                    example : username
                password:
                    type: string
                    example: Password123
            responses :
                200 :
                    description : user logged
                    schema:
                        $ref: "#/definitions/User_inst1"

                401 :
                    description: user not found
        """
        name_ = kwargs["name"]
        password_ = kwargs["password"]
        query: User = User.query.filter_by(name=name_, password=password_)
        user = query.first()
        result = user._s_jsonapi_encode()
        result = query.first()._s_jsonapi_encode()
        response = safrs.response.SAFRSResponse(status=200)
        new_data = safrs.jsonapi_format_response(result)
        # response.set_data(new_data)
        # return response
        return jsonapi.make_response(jsonify(new_data), HTTPStatus.ACCEPTED)
        # resp_data = safrs.jsonapi_format_response(result)
        # return jsonapi.make_response(resp_data, HTTPStatus.ACCEPTED)
        """
        resp_data = help_method(user, UserId=user.id)

        response = make_response(resp_data, HTTPStatus.CREATED)
        return response """


def help_method(user: User, **kwargs):
    from flask import jsonify, make_response as flask_make_response, url_for, request

    from safrs.jsonapi_formatting import jsonapi_filter_query, jsonapi_filter_list, jsonapi_sort, jsonapi_format_response, \
        paginate

    from safrs.jsonapi import make_response

    data = None
    meta = {}
    errors = None
    links = None

    object_id = user._s_object_id
    if object_id in kwargs:
        # Retrieve a single instance
        id = kwargs[object_id]
        instance = user.get_instance(id)
        data = instance
        links = {"self": instance._s_url}
        if request.url != instance._s_url:
            links["related"] = request.url
        count = 1
        meta.update(dict(instance_meta=instance._s_meta()))
    else:
        # retrieve a collection, filter and sort
        instances = user.SAFRSObject._s_get()
        instances = jsonapi_sort(instances, user.SAFRSObject)
        links, data, count = paginate(instances, user.SAFRSObject)

    # format the response: add the included objects
    result = jsonapi_format_response(data, meta, links, errors, count)
    return make_response(jsonify(result))


class Message(SAFRSBase, db.Model):
    """
        description: User description
    """
    __tablename__ = 'Messages'
    http_methods = ["get", "post", "delete"]
    exclude_attrs = ["to_user"]
    id = db.Column(db.String, primary_key=True)
    content = db.Column(db.String)
    from_user_id = db.Column(db.String)
    to_user_id = db.Column(db.String, db.ForeignKey("Users.id"))
    to_user = db.relationship("User", back_populates="incoming_messages")


def create_api():
    HOST = "127.0.0.1"
    PORT = 5000
    app = Flask("Messages server")
    app.config.update(SQLALCHEMY_DATABASE_URI="sqlite://", DEBUG=True)
    db.init_app(app)
    db.app = app
    db.create_all()
    API_PREFIX = ""
    with app.app_context():
        api = SAFRSAPI(app, host="{}".format(HOST), port=PORT, prefix=API_PREFIX)

        User(name="test1", password="test2")
        api.expose_object(User)
        api.expose_object(Message)

        print("Starting API: http://{}:{}{}".format(HOST, PORT, API_PREFIX))
        app.run(host=HOST, port=PORT)


if __name__ == "__main__":
    create_api()

from enum import unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from safrs import SAFRSBase, SAFRSAPI, jsonapi_rpc
import logging

db = SQLAlchemy()


class Message(SAFRSBase, db.Model):
    __tablename__ = "Message"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String)
    receiver = db.Column(db.String)
    sender = db.Column(db.String)

    # http_methods = ['get', 'delete']


class User(SAFRSBase, db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, index=True)

   

def create_api(app, HOST="localhost", PORT=5000, API_PREFIX=""):
    api = SAFRSAPI(app, host=HOST, port=PORT, prefix=API_PREFIX)
    #api.expose_object(Server)
    api.expose_object(User)
    api.expose_object(Message)
    print("Created API: http://{}:{}/{}".format(HOST, PORT, API_PREFIX))

def create_app(config_filename=None, host="localhost"):
    app = Flask("demo_app")
    app.debug=True
    app.logger.setLevel(logging.INFO)
    app.config.update(SQLALCHEMY_DATABASE_URI="sqlite://")
    db.init_app(app)

    with app.app_context():
        db.create_all()
        create_api(app, host)
    
    return app

host = "localhost"
app = create_app(host=host)

if __name__ == "__main__":
    app.run(host=host, debug=True)

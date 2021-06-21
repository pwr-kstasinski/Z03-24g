import pickle
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="ZiemniaczaneRozmowy", version="1.0.0")


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Message(BaseModel):
    sender: str
    content: str


with open('userlist.pickle', 'rb') as dbJester:
    users = pickle.load(dbJester)


def serialize():
    with open('users.pickle', 'wb') as dbJester:
        pickle.dump(users, dbJester, protocol=pickle.HIGHEST_PROTOCOL)


def Response(error="All OK", code=200, contents=None):
    return {"code": code, "error": error, "contents": contents}, code


@app.get('/message/{login}')
def getMessage(login):
    if login not in users:
        return Response("User nor found", 404)
    messages = users[login]
    users[login] = users[login][len(users[login]):]
    serialize()
    return Response(contents=messages)


@app.post('/message/{login}')
def postMessage(login, message_request: Message):
    if login not in users:
        return Response("User nor found", 404)
    users[login].append(message_request.json())
    serialize()
    return Response()


@app.get('/login/{login}')
def getLogin(login):
        if login not in users:
            return Response("User nor found", 404)
        return Response()


@app.get('/user/{login}')
def getUser(login):
      if login not in users:
          return Response("User nor found", 404)
      return Response(contents=[user for user in users if user != login])


@app.post('/user/{login}')
def postUser(login):
        if login in users:
            return Response("I am taken", 404)
        users[login] = []
        serialize()
        return Response()


if __name__ == '__main__':
    # serialize()
    # print(users)
    uvicorn.run('app:app', host='127.0.0.1', port=8000)

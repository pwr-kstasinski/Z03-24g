from fastapi import FastAPI, Request, Depends, WebSocket
import uvicorn
from sqlalchemy.orm import Session
import models
from database import SessionLocal, engine

import socket

models.Base.metadata.create_all(bind=engine)
from pydantic import BaseModel
from models import User, Messages
from sqlalchemy import select
from datetime import date, datetime

HEADER = 64
PORT = 5500
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
clients = []


class UserRegistration(BaseModel):
    login: str
    password: str


tags_metadata = [
    {
        "name": "messages",
        "description": "Operations with sending and receiving messages"

    },
    {
        "name": "users",
        "description": "Operations with logging and registering"
    }

]
app = FastAPI(debug=True, title="Lets Chat", description="Simple Api created to communicate between users",
              openapi_tags=tags_metadata)

global users
global common


def get_db():
    try:
        db = SessionLocal()
        yield db

    finally:
        db.close()


@app.put("/markedAsRead/{name}/{sender}", tags=["messages"], summary="Mark as read")
def markedAsRead(name: str, sender: str, db: Session = Depends(get_db)):
    flag = True
    mess = Messages()
    stmt = select(Messages).where(Messages.receiverUsername == name, Messages.senderUsername == sender,
                                  Messages.isRead == False)
    result = db.execute(stmt)

    for user_obj in result.scalars():
        flag = False
        user_obj.isRead = True
        db.commit()

    if flag:
        return {"Validation": "No new messages"}

    else:
        msg = f"9{name}"
        for i in clients:
            if i[1] == sender:
                i[0].send(msg.encode(FORMAT))

        return {"System": "Updated"}


@app.get("/getNew/{name}/{sender}", tags=["messages"], summary="Get number and content of new messages")
def getNew(name: str, sender: str, db: Session = Depends(get_db)):
    tab = []
    count = 0
    flag = True
    mess = Messages()
    stmt = select(Messages).where(Messages.receiverUsername == name, Messages.senderUsername == sender,
                                  Messages.isRead == False)
    result = db.execute(stmt)

    for user_obj in result.scalars():
        tab.append(user_obj)
        flag = False
        count += 1

    return tab, count


@app.get("/get/{name}/{sender}", tags=["messages"], summary="Receive messages")
def get(name: str, sender: str, db: Session = Depends(get_db)):
    tab = []
    mess = Messages()
    flag = True
    stmt = select(Messages).where(Messages.receiverUsername == name, Messages.senderUsername == sender,
                                  )
    result = db.execute(stmt)

    for user_obj in result.scalars():
        flag = False
        tab.append(user_obj)

    stmt2 = select(Messages).where(Messages.receiverUsername == sender, Messages.senderUsername == name,
                                   )
    result2 = db.execute(stmt2)

    for user_obj2 in result2.scalars():
        flag = False
        tab.append(user_obj2)

    return tab


@app.post("/send/{sender_username}/{receiver_username}/{message}", tags=["messages"], status_code=201,
          summary="Send message")
def post(sender_username: str, receiver_username: str, message: str, db: Session = Depends(get_db)):
    mess = Messages()

    isAlreadyInDataBase = db.query(models.User).filter(models.User.login == receiver_username).first()
    today = date.today()
    d1 = today.strftime("%Y/%m/%d")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    if isAlreadyInDataBase != None:
        mess.senderUsername = sender_username
        mess.receiverUsername = receiver_username
        mess.message = message
        mess.date = d1
        mess.time = current_time
        db.add(mess)
        db.commit()
        db.refresh(mess)

        returnMess = sender_username
        for i in clients:
            if i[1] == sender_username:
                continue
            elif i[1] == receiver_username:
                i[0].send(returnMess.encode(FORMAT))
        return {"sending": "done"}

    else:
        return {"Information": "There is no such user"}


@app.post("/sendAll", tags=["messages"], status_code=201, summary="Send message to All")
def postAll(sender_username: str, receiver_username: str, message: str, db: Session = Depends(get_db)):
    isAlreadyInDataBase = db.query(models.User).filter(models.User.login != "").all()
    today = date.today()
    d1 = today.strftime("%Y/%m/%d")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if isAlreadyInDataBase != None:
        for obj in isAlreadyInDataBase:

            if obj.login == sender_username:
                continue
            else:
                mess = Messages()
                mess.senderUsername = sender_username
                mess.receiverUsername = obj.login
                mess.message = message
                mess.date = d1
                mess.time = current_time
                mess.toAll = True
                db.add(mess)
                db.commit()
                db.refresh(mess)
                returnMess = sender_username
                for i in clients:
                    if i[1] == obj.login:
                        i[0].send(returnMess.encode(FORMAT))

    else:
        return {"Information": "There is no users"}


@app.post("/register", tags=["users"], status_code=201, summary="Register")
def put(request: UserRegistration, db: Session = Depends(get_db)):
    user = User()
    isAlreadyInDataBase = db.query(models.User).filter(models.User.login == request.login).first()

    if isAlreadyInDataBase != None:

        return {"Information": "This login is already taken"}
    else:
        user.login = request.login
        user.hashed_password = request.password
        user.is_active = 1
        db.add(user)
        db.commit()
        db.refresh(user)
        client, addr = server.accept()

        message = client.recv(1024)
        mess = message.decode(FORMAT)

        clients.append((client, mess))
        returnMess = "0"
        for i in clients:
            i[0].send(returnMess.encode(FORMAT))
        return {"Information": "Successfully created account"}


@app.post("/login", tags=["users"], status_code=201, summary="Enter your login")
def put(request: UserRegistration, db: Session = Depends(get_db)):
    flag = True

    stmt = select(User).where(User.login == request.login, User.hashed_password == request.password)
    result = db.execute(stmt)

    for user_obj in result.scalars():
        flag = False
        login = user_obj.login

        user_obj.is_active = 1
        db.commit()

    if flag:
        return {"Validation": "Invalid login or password"}

    else:
        returnMess = "0"
        for i in clients:
            if i[1] == request.login:
                continue
            else:
                i[0].send(returnMess.encode(FORMAT))
        return {"Information": f"Welcome to the Lets App:  {login}"}


@app.post("/logout", tags=["users"], status_code=201, summary="LogOut")
def logout(request: UserRegistration, db: Session = Depends(get_db)):
    print(request.login)
    stmt = select(User).where(User.login == request.login)
    result = db.execute(stmt)
    print("IM here")
    for user_obj in result.scalars():
        print(user_obj.login)
        user_obj.is_active = 0
        db.commit()
    returnMess = "0"

    for i in clients:
        if i[1] == request.login:
            continue
        else:
            i[0].send(returnMess.encode(FORMAT))


@app.get("/activeUsers", tags=["users"], status_code=201, summary="Print active users")
def activeUsers(db: Session = Depends(get_db)):
    isAlreadyInDataBase = db.query(models.User).filter(models.User.is_active == 1).all()
    allUsers = db.query(models.User).filter(models.User.is_active != 2).all()
    return isAlreadyInDataBase, allUsers


server.listen()

print(f"Server is listening on {server}")

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=5000)

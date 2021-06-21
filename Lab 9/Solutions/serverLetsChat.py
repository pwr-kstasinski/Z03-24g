
from fastapi import FastAPI, Request, Depends
import uvicorn
from sqlalchemy.orm import Session
import models
from database import SessionLocal, engine
models.Base.metadata.create_all(bind=engine)
from pydantic import BaseModel
from models import User, Messages
from sqlalchemy import select




class UserRegistration(BaseModel):
    login : str
    password : str

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
app = FastAPI(debug=True, title = "Lets Chat", description= "Simple Api created to communicate between users", openapi_tags=tags_metadata)

global users
global common
def get_db():

    try:
        db = SessionLocal()
        yield db

    finally:
        db.close()




@app.get("/get/{name}", tags=["messages"], summary="Receive messages")
def get(name: str, db : Session = Depends(get_db)):

    mess = Messages()
    isAlreadyInDataBase = db.query(models.Messages).filter(models.Messages.receiverUsername == name ).all()

    if isAlreadyInDataBase != []:

        global users
        users = isAlreadyInDataBase
        db.query(models.Messages).filter(models.Messages.receiverUsername == name).delete()
        db.commit()
        return users

    else:
        return {"Information" : "No new messages"}


@app.post("/send/{sender_username}/{receiver_username}/{message}", tags=["messages"], status_code=201, summary="Send message")
def post(sender_username: str, receiver_username: str, message: str, db : Session = Depends(get_db) ):
    pass
    mess = Messages()

    isAlreadyInDataBase = db.query(models.User).filter(models.User.login == receiver_username).first()

    if isAlreadyInDataBase != None:
        mess.senderUsername = sender_username
        mess.receiverUsername = receiver_username
        mess.message = message
        db.add(mess)
        db.commit()
        db.refresh(mess)
        return {"sending": "done"}

    else:
        return{"Information" : "There is no such user"}

@app.post("/sendAll", tags=["messages"], status_code=201, summary="Send message to All")
def post(sender_username: str , receiver_username: str ,  message: str, db : Session = Depends(get_db)):

    isAlreadyInDataBase = db.query(models.User).filter(models.User.login != "").all()

    if isAlreadyInDataBase != None:
        for obj in isAlreadyInDataBase:

            if obj.login == sender_username:
                continue
            else:
                mess = Messages()
                print(obj.login)
                mess.senderUsername = sender_username
                mess.receiverUsername = obj.login
                mess.message = message
                db.add(mess)
                db.commit()
                db.refresh(mess)


    else:
        return {"Information": "There is no users"}




@app.post("/register", tags=["users"], status_code=201, summary="Register")
def put(request: UserRegistration, db : Session = Depends(get_db)):
    pass
    user = User()
    isAlreadyInDataBase = db.query(models.User).filter(models.User.login == request.login).first()
    print(isAlreadyInDataBase)
    if isAlreadyInDataBase != None:

        return {"Information" : "This login is already taken"}
    else:
        user.login = request.login
        user.hashed_password = request.password
        user.is_active = 1
        db.add(user)
        db.commit()
        db.refresh(user)
        return {"Information" : "Successfully created account"}

@app.post("/login", tags=["users"], status_code=201, summary="Enter your login")
def put(request : UserRegistration, db : Session = Depends(get_db)):

    flag = True


    stmt = select(User).where(User.login == request.login, User.hashed_password == request.password)
    result = db.execute(stmt)

    for user_obj in result.scalars():
        flag = False
        login = user_obj.login


        user_obj.is_active = 1
        db.commit()


    if flag :
        return {"Validation": "Invalid login or password"}

    else:
        return {"Information": f"Welcome to the Lets App:  {login}"}


@app.post("/logout", tags=["users"], status_code=201, summary="LogOut")
def logout(request : UserRegistration, db : Session = Depends(get_db)):
    print(request.login)
    stmt = select(User).where(User.login == request.login)
    result = db.execute(stmt)
    print("IM here")
    for user_obj in result.scalars():
        print(user_obj.login)
        user_obj.is_active = 0
        db.commit()


@app.get("/activeUsers", tags=["users"], status_code=201, summary="Print active users")
def activeUsers(db : Session = Depends(get_db)):

    isAlreadyInDataBase = db.query(models.User).filter(models.User.is_active == 1).all()

    return isAlreadyInDataBase


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=5000)
from typing import List
from fastapi import FastAPI, Depends, HTTPException
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import and_
from sqlalchemy.orm import Session
from servo.database import  SessionLocal, engine
from servo import models, schemas

app = FastAPI(title="ZiemniaczaneRozmowy", version="1.0.0")
models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/user/',  response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.User).offset(skip).limit(limit).all()


@app.post('/user/', response_model=schemas.User)
def create_user(new_user: schemas.UserCreate, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.login == new_user.login).first()
    if user:
        raise HTTPException(status_code=400, detail="Login already registered")
    password =new_user.password
    db_user = models.User(login=new_user.login, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.post("/user/login/", response_model=schemas.User)
def login_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    logger = db.query(models.User).filter(models.User.login == user.login).filter(models.User.password == user.password).first()
    if not logger:
        raise HTTPException(status_code=404, detail="User not found")
    logger.is_active = True
    db.commit()
    db.refresh(logger)
    return logger


@app.post('/user/logout/', response_model=schemas.User)
def logout_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    logger = db.query(models.User).filter(models.User.login == user.login).first()
    if not logger:
        raise HTTPException(status_code=404, detail="User not found")
    logger.is_active = False
    db.commit()
    db.refresh(logger)
    return logger


@app.get('/user/messages/{reciver}', response_model= List[schemas.Message])
def get_messages_to_user(reciver: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    messages = db.query(models.Message)\
        .filter(and_(models.Message.reciver_id == reciver, models.Message.is_recived == False)) \
        .order_by(models.Message.id).offset(skip).limit(limit).all()
    for message in messages:
        message.is_recived = True
        db.commit()
        db.refresh(message)
    if len(messages) == 0:
        raise HTTPException(status_code=404, detail='Messages not found')
    return messages


@app.post('/user/messages/', response_model= schemas.Message)
def create_message(message: schemas.MessageCreate, reciver: schemas.UserBase, db: Session = Depends(get_db)):
    db_reciver = db.query(models.User).filter(models.User.login == reciver.login).first()
    if not db_reciver:
        raise HTTPException(status_code=404, detail="User not found")
    db_message = models.Message(**message.dict(), reciver_id=db_reciver.id)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message


if __name__ == '__main__':
    uvicorn.run('app:app', host='127.0.0.1', port=8000)

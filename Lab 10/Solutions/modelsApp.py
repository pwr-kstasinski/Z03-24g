from sqlalchemy import Boolean, Column, Integer, String

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

class Messages(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    senderUsername = Column(String)
    receiverUsername = Column(String)
    message = Column(String)
    date = Column(String)
    time = Column(String)
    isRead = Column(Boolean, default=False)
    toAll = Column(Boolean, default=False)







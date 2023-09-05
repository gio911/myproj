from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, LargeBinary, Boolean
from database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__='users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

#1.1  #Define a one-to-many relationship between User and Payment
    payments = relationship('Payment', back_populates='creator')

#2.1  #Define a one-to-many relationship between User and Comment
    commentments = relationship("Commentment", back_populates="author")


class Payment(Base):
    __tablename__='payments'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, default=datetime.utcnow)
    num = Column(Integer, unique=True)
    sum = Column(Integer)
    counterparty = Column(String)
    contract = Column(String)
    purpose = Column(String)
    comment = Column(String)
    document = Column(LargeBinary)
    pdfsrc = Column(String)
    wordsrc = Column(String)
    doccreated = Column(Boolean, default=False)
    docarchive = Column(Boolean, default=False)

    user_id = Column(Integer, ForeignKey('users.id'))
    
#1.2 #OWNER Define a many-to-one relationship between Payment and User
    creator = relationship("User", back_populates="payments")
#3.1 # Define a one-to-many relationship between Payment and Comment
    commentments = relationship("Commentment", back_populates="payments")


class Commentment(Base):
    __tablename__='comments'

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    isDone = Column(Boolean, default=False)    

    payment_id = Column(Integer, ForeignKey('payments.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

#2.2 # Define a many-to-one relationship between Comment and User
    author = relationship('User', back_populates='commentments')
#3.2 # Define a many-to-one relationship between Comment and Payment
    payments = relationship('Payment', back_populates='commentments')
    
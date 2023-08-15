from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from database import Base
from sqlalchemy.orm import relationship


class Customer(Base):
    __tablename__='customers'

    id = Column(Integer, primary_key=True, index=True)
    payment_date = Column(DateTime, default=datetime.utcnow)
    payment_num = Column(Integer, unique=True)
    payment_sum = Column(Integer)
    counterparty = Column(String)
    contract = Column(String)
    payment_purpose = Column(String)
    comment = Column(String)

    user_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship("User", back_populates="customers")

class User(Base):
    __tablename__='users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    customers = relationship('Customer', back_populates='creator')

from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, LargeBinary, Boolean
from database import Base
from sqlalchemy.orm import relationship


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
    docsrc = Column(String)
    doccreated = Column(Boolean, default=False)
    docarchive = Column(Boolean, default=False)

    user_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship("User", back_populates="payments")

class User(Base):
    __tablename__='users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    payments = relationship('Payment', back_populates='creator')

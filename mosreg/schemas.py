from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
# current_payments
class PaymentBase(BaseModel):
    date:datetime
    num:int
    sum:int
    counterparty:str
    contract:str
    purpose:str = None
    comment:str
    
class Payment(PaymentBase):
    class Config():
        orm_mode=True
    
class PaymentWithId(PaymentBase):
    id:int
    class Config():
        orm_mode=True

class User(BaseModel):
    name:str
    email:str
    password:str

class UserWithId(User):
    id:int
    class Config():
        orm_mode=True
    
class ShowUser(BaseModel):
    name:str
    email:str
    payments:List[Payment]=[]

    class Config():
        orm_mode=True

class ShowPayment(BaseModel):
    id:int
    counterparty:str
    creator:ShowUser

    class Config():
        orm_mode=True


class Login(BaseModel):
    username:str
    password:str



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
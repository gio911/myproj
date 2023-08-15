from datetime import date
from typing import List, Optional
from pydantic import BaseModel

class CustomerBase(BaseModel):
    payment_date:date
    payment_num:int
    payment_sum:int
    counterparty:str
    contract:str
    payment_purpose:str = None
    comment:str
    
class Customer(CustomerBase):
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
    customers:List[Customer]=[]

    class Config():
        orm_mode=True

class ShowCustomer(BaseModel):
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
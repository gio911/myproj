from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class PDFResponse(BaseModel):
    filename: str
    content_type: str

class Commentment(BaseModel):
    id:int
    date:datetime
    text: str
    isDone: bool
    payment_id: int
    user_id: int

class PaymentBase(BaseModel):
    date:datetime
    num:int
    sum:int
    counterparty:str
    contract:str
    purpose:str = None
    comment:str
    pdfsrc:str = None
    wordsrc:str = None
    doccreated:bool = False
    docarchive:bool = False
    
class Payment(PaymentBase):
    class Config():
        orm_mode=True
    
class PaymentWithId(PaymentBase):
    id:int
    user_id:int
    class Config():
        orm_mode=True

class PaymentWithWord(PaymentBase):
    id:int
    document:bytes
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

class PaymentWithCommentment(PaymentBase):
    commentments:List[Commentment]

    class Config():
        orm_mode=True
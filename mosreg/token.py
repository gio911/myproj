from datetime import timedelta, datetime
from typing import Union

from fastapi import Depends

from database import SessionLocal, get_db
from mosreg import models
from . import schemas
from jose import JWTError, jwt
from sqlalchemy.orm import Session

db=SessionLocal()

def get_user(username):
    user = db.query(models.User).filter(models.User.email==username).first()
    print(user, 999)
    return user
    

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token:str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=username)
    except JWTError:
        raise credentials_exception
    user = get_user(username=token_data.email)
    print('in ver_tok', user.name)
    return user
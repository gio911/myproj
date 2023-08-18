from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
from mosreg.hashing import Hash

from mosreg import models, schemas, token


router = APIRouter(
    prefix='/api/login',
    tags = ['Authentication']
)

@router.post('/')
def login(request:OAuth2PasswordRequestForm = Depends(), db:Session=Depends(get_db)):

    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail='Invalid credantials')
    if not Hash.verify(request.password, user.password):
        print(request.username, 'request.username')
        print(user.password, 'user.password,')

        print(user.name, user.email, user.password, 22222)

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail='Incorrect password')
    access_token = token.create_access_token(data={"sub": user.email})
    print(access_token, 'access_token')
    return {"access_token": access_token, "token_type": "bearer"}
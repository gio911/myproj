from typing import List
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from database import get_db
from mosreg.oauth2 import get_current_user
from ..services import user
from mosreg import models, schemas, services

router = APIRouter(
    prefix='/api/user',
    tags=['Users']
)

@router.post('/', response_model=schemas.ShowUser)
def create_user(request:schemas.User, db:Session=Depends(get_db)):
    return user.create_user(request, db)

@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id:int, db:Session=Depends(get_db), current_user:schemas.User=Depends(get_current_user)):
    print(current_user.name,43434222)
    return user.get_user(id, db, current_user)


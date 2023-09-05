import statistics
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from fastapi import APIRouter
from database import get_db
from mosreg import models, schemas
from mosreg.oauth2 import get_current_user
from mosreg.services import commentmen


router = APIRouter(
    prefix='/api/comments',
    tags = ['Commentments']
)

@router.get('/{id}')
def get_all_commentments(id:int, db:Session=Depends(get_db), current_user:schemas.User=Depends(get_current_user)):
    return commentmen.get_all(id, db, current_user)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.Commentment)
def create(request:schemas.Commentment, db:Session=Depends(get_db), current_user:schemas.User=Depends(get_current_user)):
    return commentmen.create_commentment(request, db, current_user) 

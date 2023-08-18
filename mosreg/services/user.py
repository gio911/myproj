from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from mosreg import models, schemas
from mosreg.hashing import Hash
from mosreg.oauth2 import get_current_user

def create_user(request:schemas.User, db:Session):
    print(request, 888)
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user) 
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(id:int, db:Session, current_user:schemas.UserWithId=Depends(get_current_user)):
    user = db.query(models.User).filter(models.User.id==current_user.id).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with the id {id} is not avalable')
    return user


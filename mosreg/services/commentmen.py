import statistics
from fastapi import Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from database import get_db
from mosreg import models, schemas
from mosreg.oauth2 import get_current_user



def get_all(id:int, db:Session=Depends(get_db), current_user:schemas.User=Depends(get_current_user)):
    
    new_comment = db.query(models.Commentment).filter(models.Commentment.user_id==current_user.id).filter(models.Commentment.payment_id==id).all()
   
    return new_comment    


def create_commentment(id:int, request:schemas.Commentment, db:Session=Depends(get_db), current_user:schemas.User=Depends(get_current_user)):
    
    new_comment = models.Commentment(text=request.text, payment_id=id)
    db.add(new_comment)
    db.refresh(new_comment)
    return new_comment    

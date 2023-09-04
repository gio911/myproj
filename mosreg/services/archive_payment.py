import statistics
from fastapi import Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from database import get_db
from mosreg import models, schemas
from mosreg.oauth2 import get_current_user



def get_all(db:Session=Depends(get_db), current_user:schemas.User=Depends(get_current_user)):
    payments = db.query(models.Payment).filter(models.Payment.user_id==current_user.id).filter(models.Payment.docarchive==True).all()

    return payments


def delete(id:int, db:Session=Depends(get_db), current_user:schemas.User=Depends(get_current_user)):
    payment=db.query(models.Payment).filter(models.Payment.user_id==current_user.id).filter(models.Payment.id==id)
    if not payment.first():
        raise HTTPException(status_code=statistics.HTTP_404_NOT_FOUND,
                            detail=f'Payment for delitting with the id {id} was not found')
    payment.delete(synchronize_session=False)
    db.commit()
    return 'Платеж удален'

def fetch_pdf(id:int, request:schemas.PaymentWithId, db:Session=Depends(get_db), current_user:schemas.User=Depends(get_current_user)):
    
    payment = db.query(models.Payment).filter(models.Payment.user_id==current_user.id).filter(models.Payment.id==id).first()
    
    pdf_path = payment.pdfsrc
    print( 44443434)
    return FileResponse(pdf_path, media_type="application/pdf")

def back_payment(id:int, db:Session=Depends(get_db), current_user:schemas.UserWithId=Depends(get_current_user)):
    payment = db.query(models.Payment).filter(models.Payment.user_id==current_user.id).filter(models.Payment.id==id).first()
    payment.docarchive=False
    db.commit()
    return 'Перенесено в текущие платежи'
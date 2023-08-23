from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from mosreg import models, schemas
from mosreg.oauth2 import get_current_user
from utils.to_word import generate_document


def get_all(db:Session = Depends(get_db), current_user:schemas.UserWithId=Depends(get_current_user)):
    print(333)
    payments = db.query(models.Payment).filter(models.Payment.user_id==current_user.id).all()
    print(4444)
    return payments

def create(request:schemas.Payment, db:Session = Depends(get_db), current_user:schemas.UserWithId=Depends(get_current_user)):
    new_payment = models.Payment(counterparty=request.counterparty, num=request.num, sum=request.sum, contract=request.contract, purpose=request.purpose, comment=request.comment, user_id=current_user.id)
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)
    return new_payment    

def delete(id:int, db:Session = Depends(get_db), current_user:schemas.UserWithId=Depends(get_current_user)):
    payment = db.query(models.Payment).filter(models.Payment.user_id==current_user.id).filter(models.Payment.id  
                                                ==id)
    if not payment.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Payment for delitting with the id {id} was not found')
    payment.delete(synchronize_session=False)
    db.commit()
    return {'deleted'}

def update(id:int,request:schemas.Payment, db:Session = Depends(get_db), current_user:schemas.UserWithId=Depends(get_current_user)):
    print(request, 'requestrequestrequest')
    payment = db.query(models.Payment).filter(models.Payment.user_id==current_user.id).filter(models.Payment.id==id)
    if not payment.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Payment for udating with the id {id} was not found')
    payment.update({'counterparty':request.counterparty})
    db.commit()
    return {'updated'}

def get_payment(id:int, db:Session = Depends(get_db), current_user:schemas.UserWithId=Depends(get_current_user)):
    payment = db.query(models.Payment).filter(models.Payment.user_id==current_user.id).filter(models.Payment.id==id).first()
    if not payment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Payment with the id {id} is not avalable')
    return payment

def to_word(id:int, request:schemas.Payment, db:Session = Depends(get_db), current_user:schemas.UserWithId=Depends(get_current_user)):
    payment = db.query(models.Payment).filter(models.Payment.user_id==current_user.id).filter(models.Payment.id==id).first()
    document_buffer = generate_document(request)
    payment.document = document_buffer.read()
    db.commit()
    
    return {'generated'}
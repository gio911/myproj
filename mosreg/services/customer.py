from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from mosreg import models, schemas
from mosreg.oauth2 import get_current_user


def get_all(db:Session = Depends(get_db), current_user:schemas.UserWithId=Depends(get_current_user)):
    customers = db.query(models.Customer).filter(models.Customer.user_id==current_user.id).all()
    print(customers, 9990)
    return customers

def create(request:schemas.Customer, db:Session = Depends(get_db), current_user:schemas.UserWithId=Depends(get_current_user)):
    new_customer = models.Customer(counterparty=request.counterparty, payment_num=request.payment_num, payment_sum=request.payment_sum, contract=request.contract, payment_purpose=request.payment_purpose, comment=request.comment, user_id=current_user.id)
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer    

def delete(id:int, db:Session = Depends(get_db), current_user:schemas.UserWithId=Depends(get_current_user)):
    customer = db.query(models.Customer).filter(models.Customer.user_id==current_user.id).filter(models.Customer.id  
                                                ==id)
    if not customer.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Customer for delitting with the id {id} was not found')
    customer.delete(synchronize_session=False)
    db.commit()
    return {'deleted'}

def update(id:int,request:schemas.Customer, db:Session = Depends(get_db), current_user:schemas.UserWithId=Depends(get_current_user)):
    customer = db.query(models.Customer).filter(models.Customer.user_id==current_user.id).filter(models.Customer.id==id)
    if not customer.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Customer for udating with the id {id} was not found')
    customer.update({'name':request.name})
    db.commit()
    return {'updated'}

def get_customer(id:int, db:Session = Depends(get_db), current_user:schemas.UserWithId=Depends(get_current_user)):
    customer = db.query(models.Customer).filter(models.Customer.user_id==current_user.id).filter(models.Customer.id==id).first()
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Customer with the id {id} is not avalable')
    return customer
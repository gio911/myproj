from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from mosreg.oauth2 import get_current_user
from ..services import payment 

from mosreg import models, schemas

router = APIRouter( 
    prefix='/api/currentpayments',
    tags=['Payments'],
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request:schemas.Payment, db:Session = Depends(get_db), current_user:schemas.User=Depends(get_current_user)):
    return payment.create(request, db, current_user)


@router.get('/', response_model=List[schemas.ShowPayment])
def all_payments(db:Session = Depends(get_db), current_user:schemas.User=Depends(get_current_user)):
    return payment.get_all(db, current_user)


@router.get('/{id}', response_model=schemas.ShowPayment)
def get_specific_payment(id:int, db:Session = Depends(get_db), current_user:schemas.User=Depends(get_current_user)):
    return payment.get_payment(id, db, current_user)

@router.delete('/{id}')
def delet_payment(id, db:Session=Depends(get_db), current_user:schemas.User=Depends(get_current_user)):
    return payment.delete(id, db, current_user)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_payment(id:int, request:schemas.Payment, db:Session=Depends(get_db), current_user:schemas.User=Depends(get_current_user)):
    return payment.update(id, request, db, current_user)

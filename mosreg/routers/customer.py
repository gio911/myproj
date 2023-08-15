from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from mosreg.oauth2 import get_current_user
from ..services import customer 

from mosreg import models, schemas

router = APIRouter( 
    prefix='/api/customer',
    tags=['Customers'],
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request:schemas.Customer, db:Session = Depends(get_db), current_user:schemas.User=Depends(get_current_user)):
    return customer.create(request, db, current_user)


@router.get('/', response_model=List[schemas.ShowCustomer])
def all_customers(db:Session = Depends(get_db), current_user:schemas.User=Depends(get_current_user)):
    return customer.get_all(db, current_user)


@router.get('/{id}', response_model=schemas.ShowCustomer)
def get_specific_customer(id:int, db:Session = Depends(get_db), current_user:schemas.User=Depends(get_current_user)):
    return customer.get_customer(id, db, current_user)

@router.delete('/{id}')
def delet_customer(id, db:Session=Depends(get_db), current_user:schemas.User=Depends(get_current_user)):
    return customer.delete(id, db, current_user)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_customer(id:int, request:schemas.Customer, db:Session=Depends(get_db), current_user:schemas.User=Depends(get_current_user)):
    return customer.update(id, request, db, current_user)

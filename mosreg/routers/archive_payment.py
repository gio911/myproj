from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from mosreg import schemas
from mosreg.oauth2 import get_current_user
from ..services import archive_payment 
from fastapi.responses import FileResponse
from reportlab.pdfgen import canvas

router = APIRouter( 
    prefix='/api/archive-payments',
    tags=['Payments'],
)

@router.get('/', response_model=List[schemas.PaymentWithId])
def get_all_archive_payments(db:Session=Depends(get_db), current_user:schemas.User=Depends(get_current_user)):
    return archive_payment.get_all(db, current_user)

@router.delete('/{id}', response_model=str)
def delete_archive_payment(id, db:Session=Depends(get_db), current_user:schemas.UserWithId=Depends(get_current_user)):
    return archive_payment.delete(id, db, current_user)

@router.post('/fetch-pdf/{id}', response_model=str)
def fetch_pdf(id:int, request:schemas.Payment, db:Session=Depends(get_db), current_user:schemas.User=Depends(get_current_user)):

    return archive_payment.fetch_pdf(id, request, db, current_user)

@router.post('/back-to-current-payments/{id}', response_model=str)
def back_to_current_payments(id:int, db:Session=Depends(get_db), current_user:schemas.UserWithId=Depends(get_current_user)):
    return archive_payment.back_payment(id, db, current_user)

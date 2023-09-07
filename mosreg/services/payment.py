import os
from fastapi import Depends, HTTPException, status
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from pdf2docx import Converter

from database import get_db
from mosreg import models, schemas
from mosreg.oauth2 import get_current_user
from utils.pdf_pattern import pdf_pattern_creation

from utils.send_file_email import sendpdf


def get_all(db:Session = Depends(get_db), current_user:schemas.UserWithId=Depends(get_current_user)):
    print(333)
    payments = db.query(models.Payment).filter(models.Payment.user_id==current_user.id).filter(models.Payment.docarchive==False).all()
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

def create_pdf(id:int, request:schemas.PaymentWithId, db:Session = Depends(get_db), current_user:schemas.UserWithId=Depends(get_current_user)):
    payment = db.query(models.Payment).filter(models.Payment.user_id==current_user.id).filter(models.Payment.id==id).first()
    
    if not payment:
        raise HTTPException(status_code=404, detail='Payment not found')
    uload_folder_pdf='./uploads/pdf'
    uload_folder_word='./uploads/word'

    pdf_filename=f'payment_{request.num}_pdf.pdf'
    word_filename=f'payment_{request.num}_word.docx'

    pdf_path= os.path.join(uload_folder_pdf, pdf_filename)
    word_path= os.path.join(uload_folder_word, word_filename)
    
    pdf_pattern_creation(pdf_path, request)

    payment.pdfsrc = pdf_path

    cv = Converter(pdf_path)
    cv.convert(word_path, start=0, end=None)
    cv.close()

    payment.wordsrc = word_path
    payment.doccreated = True
    db.commit()

    return payment

def fetch_pdf(id:int, request:schemas.PaymentWithId, db:Session=Depends(get_db), current_user:schemas.User=Depends(get_current_user)):
    
    payment = db.query(models.Payment).filter(models.Payment.user_id==current_user.id).filter(models.Payment.id==id).first()
    
    pdf_path = payment.pdfsrc
    print( 44443434)
    return FileResponse(pdf_path, media_type="application/pdf")

def email_sending(id:int, request:schemas.PaymentWithId, db:Session=Depends(get_db), current_user:schemas.User=Depends(get_current_user)):
    payment = db.query(models.Payment).filter(models.Payment.user_id==current_user.id).filter(models.Payment.id==id).first()

    file_path=request.wordsrc

    uploads_word_path='./uploads/word'
    word_filename = os.path.basename(file_path)
    
    print(word_filename, 'pdf_filename')
    print(file_path, 'file_path')
    k = sendpdf(
        'syberdynesys@gmail.com',
        'syberdynesys@gmail.com',
        os.environ.get('EMAIL_PASSWORD'),
        'word document',
        'body of message',
        word_filename,
        uploads_word_path
    )

    k.email_send()
    payment.docarchive = True
    first_commentment = models.Commentment(text='Письмо отправлено на почту', user_id=current_user.id, payment_id=payment.id)

    db.add(first_commentment)
    db.commit()
    db.refresh(first_commentment)
    db.commit()

    db.close()
    return 'Письмо отправлено'
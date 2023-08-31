import os
import smtplib
from fastapi import Depends, HTTPException, status
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from database import get_db
from mosreg import models, schemas
from mosreg.oauth2 import get_current_user
from utils.to_word import generate_document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from email.message import EmailMessage
import ssl
import imghdr

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

def create_pdf(id:int, request:schemas.PaymentWithId, db:Session = Depends(get_db), current_user:schemas.UserWithId=Depends(get_current_user)):
    payment = db.query(models.Payment).filter(models.Payment.user_id==current_user.id).filter(models.Payment.id==id).first()
    
    if not payment:
        raise HTTPException(status_code=404, detail='Payment not found')
    uload_folder='./uploads'
    pdf_filename=f'payment_{request.num}_pdf.pdf'
    pdf_path= os.path.join(uload_folder, pdf_filename)

    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.drawString(100, 750, f'Hello {request.counterparty}')
    c.save()

    payment.docsrc = pdf_path
    payment.doccreated = True
    payment.docarchive = True
    db.commit()

    # document_buffer = generate_document(request)
    # print(type(document_buffer),90000000)
    # print(document_buffer,90000000)
    # payment.document = document_buffer
    # db.commit()
    return payment


def fetch_pdf(id:int, request:schemas.PaymentWithId, db:Session=Depends(get_db), current_user:schemas.User=Depends(get_current_user)):
    
    payment = db.query(models.Payment).filter(models.Payment.user_id==current_user.id).filter(models.Payment.id==id).first()


    
    pdf_path = payment.docsrc
    print( 44443434)

    # c = canvas.Canvas(pdf_path)
    # c.drawString(100, 750, "Hello, PDF!")
    # c.save()
    return FileResponse(pdf_path, media_type="application/pdf")

def email_sending(id:int, request:schemas.PaymentWithId, db:Session=Depends(get_db), current_user:schemas.User=Depends(get_current_user)):
    # payment = db.query(models.Payment).filter(models.Payment.user_id==current_user.id).filter(models.Payment.id==id).first()

    # email_password = os.environ.get('EMAIL_PASSWORD')
    # print(email_password,9494)
    # subject = 'HELLO SUBJECT'
    # body="""Rock-n-Roll baby"""
    # email_to = 'syberdynesys@gmail.com'
    # from_email='syberdynesys@gmail.com'
   
    # msg = EmailMessage()
    # msg.set_content(body)
    # msg['Subject'] = subject
    # msg['From'] = from_email
    # msg['To'] = email_to


    # context = ssl.create_default_context()
    # # # Read the PDF file content
    # # with open(file_path, "rb") as pdf_file:
    # #     pdf_content = pdf_file.read()

    # # Attach the PDF file
    # # pdf_filename = os.path.basename(file_path)
    # # msg.add_attachment(pdf_content, maintype='application', subtype='pdf', filename=pdf_filename)

    # with smtplib.SMTP('smtp.gmail.com', 587, context) as smtp:
    #     # smtp.starttls()
    #     smtp.login(from_email, email_password)
    #     smtp.send_message(from_email, email_to, msg.as_string())

    # # server.starttls()
    # # try:
    # #     server.

    # #     return "Email sent successfully"
    # # except Exception as e:
    # #     raise HTTPException(status_code=500, detail=str(e))

    # sender = 'syberdynesys@gmail.com'
    # password = os.environ.get('EMAIL_PASSWORD')

    # msg=EmailMessage()

    # with open(file_path, 'rb') as f:
    #     file_data= f.read()
    #     file_type = imghdr.what(f.name)
    #     file_name=f.name

    # print(file_path, file_type, file_name, 9494940000000000)

    # msg.add_attachment(file_data, maintype='multipart', subtype=file_type, filename=file_name)

    # server = smtplib.SMTP('smtp.gmail.com', 587)

    # server.starttls()



    # try:
    #     server.login(sender, password)
    #     server.sendmail(sender, sender,msg)

    #     return 'OK'
    # except Exception as _ex:
    #     return '555'



    from pdf_mail import sendpdf

    file_path=request.docsrc

    uploads_path='./uploads'
    pdf_filename = os.path.basename(file_path)
    pdf_filename = pdf_filename.split('.')[0]
    print(pdf_filename, 'pdf_filename')
    print(file_path, 'file_path')
    k = sendpdf(
        'syberdynesys@gmail.com',
        'syberdynesys@gmail.com',
        os.environ.get('EMAIL_PASSWORD'),
        'pdf document',
        'body of message',
        pdf_filename,
        uploads_path
    )

    k.email_send()

    return 'File was sent'
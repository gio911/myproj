import os
from datetime import datetime
from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.models import Variable
#from database import SessionLocal
# from ..mosreg import models
#from .. import models
# from utils.excel_parser import from_excel_to_dict

#db=SessionLocal()
import openpyxl
import unicodedata

###############################
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine

#from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

DATABASE_URL = f"postgresql://postgres:123321@localhost:5432/postgres"
Base = declarative_base()

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

db = SessionLocal()
##########################
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship


class Payment(Base):
    __tablename__='payments'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, default=datetime.utcnow)
    num = Column(Integer, unique=True)
    sum = Column(Integer)
    counterparty = Column(String)
    contract = Column(String)
    purpose = Column(String)
    comment = Column(String)

    user_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship("User", back_populates="payments")

class User(Base):
    __tablename__='users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    payments = relationship('Payment', back_populates='creator')
##########################

def from_excel_to_dict(file_path='/Users/gio/Desktop/myproj/data/76.xlsx', sheet_name=u'Лист1'):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb[sheet_name]
    data_dict = {}
    total_list = []
    worker_list=['Кожурин Сергей Сергеевич', 'Емелькин Василий Анатольевич', 'Афонин Алексей Геннадьевич', 'Шляпников Гурий Александрович']

    for row in sheet.iter_rows(min_row=9, values_only=True):  # Assuming the first row contains column headers
        worker = str(row[11])
        normolize_worker=unicodedata.normalize('NFC', worker)
        if normolize_worker in worker_list:
            if normolize_worker not in data_dict:
                data_dict[normolize_worker]=[{'payment_date':row[4], 'payment_num':row[3], 'payment_sum':row[5], 'counterparty':row[6], 'contract':row[7], 'comment':row[12]}]
            else:
                
                data_dict[normolize_worker].extend([{'payment_date':row[4], 'payment_num':row[3], 'payment_sum':row[5], 'counterparty':row[6], 'contract':row[7], 'comment':row[12]}])
  ##  print(data_dict, 94)
    all_users = db.query(User).all()
    print(data_dict, all_users,  9494)
    for worker in data_dict:
        print(worker, 92222)
        
        current_user = db.query(User).filter(User.name==worker).first()
        if current_user:
            print('YES')
            for payment in data_dict[worker]:
                new_payment = Payment(counterparty=payment['counterparty'], 
                                      num=payment['payment_num'], 
                                      sum=payment['payment_sum'], 
                                      date=payment['payment_date'], 
                                      contract=payment['contract'], 
                                      comment=payment['comment'], 
                                      user_id=current_user.id)
                db.add(new_payment)
                db.commit()
        else:
            continue
    return data_dict

def save_to_db(ti):
    excel_data = ti.xcom_pull(task_ids=['from_excel_to_dict_process'])
    if not excel_data:
        raise Exception('No excel data')
    all_users = db.query(User).all()
    print(excel_data, all_users,  9494)

    return excel_data

with DAG(
    dag_id='first_airflow_dag',
    schedule_interval='* * * * *',
    start_date=datetime(year=2023, month=7, day=1),
    catchup=False
) as dag:

    task_from_excel_to_dict = PythonOperator(
        task_id='from_excel_to_dict_process',
        python_callable=from_excel_to_dict
    )

    task_save_to_db = PythonOperator(
        task_id = 'save_to_db_process',
        python_callable = save_to_db
    )

    task_from_excel_to_dict >> task_save_to_db

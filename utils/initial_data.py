from sqlalchemy import create_engine
from mosreg import models
from mosreg.hashing import Hash
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=True)

#Base = declarative_base()
#Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
db=Session()
    

def database_initialization(request):
    new_user = models.User( name=str(request['name']), 
                            email=str(request['email']), 
                            password=Hash.bcrypt(request['password']))
    db.add(new_user) 
    db.commit()
    
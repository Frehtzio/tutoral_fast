from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

#SQLALCHEMY_DATABASE_URL = "postgresql://<USERNAME>:<password>@<ip_addres/hostname>/<databasename>"

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOSTNAME}:5432/{settings.DATABASE_NAME}"


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush= False, bind = engine)


Base = declarative_base()

def get_db():
    db = SessionLocal()
  
    try:
        yield db
    finally:
        db.close()
    


"""

from psycopg2.extras import RealDictCursor

import time
import psycopg2

# create dependecy
while True:
    try:
        conn = psycopg2.connect(host = 'localhost',database="fastapi",user='postgres',
                        password='hola',cursor_factory = RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succesfull!")
        break
    except Exception as error:
        print("Connection to Database failed")
        print("the error was",error)
        time.sleep(2)
    
"""


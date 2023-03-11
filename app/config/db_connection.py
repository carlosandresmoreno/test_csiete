"""
configuration file to create connection with mysql database
"""

import os

# environment variables
from dotenv import load_dotenv

# sqlalchemy libraries
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

db_name = os.getenv("DBNAME")
user_name = os.getenv("USER")
password = os.getenv("PASSWORD")
host = os.getenv("HOST")
port = os.getenv("PORT")

try:
    DATABASE = "mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8" % (
        user_name,
        password,
        host,
        port,
        db_name,
    )
    engine = create_engine(DATABASE)

    conn = engine.connect()
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    Base = declarative_base()

except OperationalError as err:
    print("ERRRORFOUND: %s" % err)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

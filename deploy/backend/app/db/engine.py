import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DB_TYPE = os.getenv("DB_TYPE")

if DB_TYPE == "LOCAL_POSTGRES":
    USER = "postgres"
    PWD = "super_password"
    DB_NAME = "ckn_db"
    HOST = "localhost"
    PORT = "5432"
    SQLALCHEMY_DATABASE_URL = f"postgresql://{USER}:{PWD}@{HOST}:{PORT}/{DB_NAME}"

    engine = create_engine(SQLALCHEMY_DATABASE_URL)

elif DB_TYPE == "LOCAL_SQLITE":
    SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
else:
    print("SET DB_TYPE FOR DEBUGGING")

if DB_TYPE == "LOCAL_POSTGRES" or DB_TYPE == "LOCAL_SQLITE":
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()

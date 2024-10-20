from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv, find_dotenv
from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session


load_dotenv(find_dotenv())

SQLALCHEMY_DATABASE_URL = "sqlite:///./income.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={'check_same_thread': False}
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


dp_dependency = Annotated[Session, Depends(get_db)]
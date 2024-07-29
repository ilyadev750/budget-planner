from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

# from . import crud, models, schemas
from models import Base
from database import SessionLocal, engine


Base.metadata.create_all(bind=engine)

app = FastAPI()
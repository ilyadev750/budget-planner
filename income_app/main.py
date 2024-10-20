from fastapi import Depends, FastAPI, HTTPException
from router import router as income_router
from models import Base
from database import SessionLocal, engine


Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(income_router)

from fastapi import Depends, FastAPI, HTTPException
import uvicorn
from api.v1.routes import routers as income_router
from models.incomes import Base
from db.database import SessionLocal, engine


Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(income_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

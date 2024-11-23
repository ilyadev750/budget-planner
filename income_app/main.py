from fastapi import FastAPI
import uvicorn
from api.v1.routes import routers as income_router
from models.incomes import Base
from db.database import engine


Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(income_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

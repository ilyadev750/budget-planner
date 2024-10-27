from fastapi import FastAPI
from db.database import Base
from db.database import engine
from api.v1.routes import routers as v1_routers

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(v1_routers)

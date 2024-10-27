from api.v1.auth import router as auth_router
from fastapi import APIRouter


routers = APIRouter()
router_list = [auth_router]


for router in router_list:
    routers.include_router(router)

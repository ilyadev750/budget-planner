from api.v1.incomes import router as income_router
from fastapi import APIRouter


routers = APIRouter()
router_list = [income_router]


for router in router_list:
    routers.include_router(router)

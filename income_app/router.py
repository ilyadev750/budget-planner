from fastapi import APIRouter 
from sqlalchemy import select
from starlette import status
from database import dp_dependency
from schema import IncomeBase
from models import Income


router = APIRouter(prefix='/incomes', tags=['Работа с доходами'])


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_income(db: dp_dependency, request: IncomeBase):
    income_model = Income(**request.dict())
    db.add(income_model)
    db.commit()
    # income_model = Income(user_id=request.user_id,
    #                       income_type_id=request.income_type_id,
    #                       income = request.income,
    #                       )
    # db.add(income_model)
    # db.commit()
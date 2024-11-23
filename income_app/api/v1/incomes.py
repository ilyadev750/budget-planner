from fastapi import APIRouter, Depends
from starlette import status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from api.v1.dependencies import user_dependency
from datetime import datetime
from schemas.incomes import IncomeBase, TypeIncomeBase, UserIncomeBase
from models.incomes import Income, TypeIncome
from typing import Annotated
from api.v1.dependencies import income_service, type_income_service
from repositories.incomes import IncomeRepository
from api.v1.dependencies import income_repository, credentials


router = APIRouter(prefix='/incomes', tags=['Работа с доходами'])


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_income(credentials: credentials,
                        user: user_dependency,
                        income_service: income_service,
                        IncomeRequest: IncomeBase):
    income_dict = IncomeRequest.model_dump()
    income_model = await income_service.create(income_dict)
    return income_model


@router.get("/get-incomes/{user_id}", status_code=200)
async def get_user_incomes(credentials: credentials,
                           user: user_dependency,
                           income_service: income_service,
                           user_id: int,
                           starttime: datetime,
                           endtime: datetime):
    """ Получить доходы пользователя за выбранный период"""
    income_dict = {'user_id': user_id,
                   'starttime': starttime,
                   'endtime': endtime}
    incomes = await income_service.get_user_incomes(income_dict)
    return incomes


@router.post("/create-income-type", status_code=200)
async def create_income_type(credentials: credentials,
                             user: user_dependency,
                             type_income_service: type_income_service,
                             TypeIncomeRequest: TypeIncomeBase):
    type_income_dict = TypeIncomeRequest.model_dump()
    result = await type_income_service.create(type_income_dict)
    return result


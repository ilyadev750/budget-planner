from typing import Annotated
from fastapi import Depends
from db.database import SessionLocal
from .auth import get_current_user
from services.incomes import IncomeService
from models.incomes import Income, TypeIncome
from repositories.incomes import IncomeRepository
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


def get_income_service():
    income_service = IncomeService(
        session=SessionLocal,
        model=Income,
        income_repo=IncomeRepository
    )
    return income_service


def get_type_income_service():
    income_service = IncomeService(
        session=SessionLocal,
        model=TypeIncome,
        income_repo=IncomeRepository
    )
    return income_service


income_repository = None
credentials = Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())]
user_dependency = Annotated[dict, Depends(get_current_user)]
income_service = Annotated[IncomeService, Depends(get_income_service)]
type_income_service = Annotated[IncomeService, Depends(get_type_income_service)]
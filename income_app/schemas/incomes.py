from pydantic import BaseModel, Field
from datetime import datetime


class TypeIncomeBase(BaseModel):
    type: str


class IncomeBase(BaseModel):
    user_id: int = Field(gt=0)
    income_type_id: int = Field(gt=0)
    income: float = Field(gt=0)


class UserIncomeBase(BaseModel):
    starttime: datetime
    endtime: datetime

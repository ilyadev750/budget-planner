from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
import datetime

from database import Base


class TypeIncome(Base):
    __tablename__ = "income_types"
    id = Column(Integer, primary_key=True)
    type = Column(String, unique=True)

    incomes = relationship("Income", back_populates="type_income")


class Income(Base):
    __tablename__ = "incomes"
    id = Column(Integer, primary_key=True)
    income = Column(Integer)
    type = Column(Integer, ForeignKey("income_types.id"))
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.now())
    edited_at = Column(DateTime(timezone=True), default=datetime.datetime.now())
    user_id = Column(Integer)
    incomes = relationship("Income", back_populates="type_income")

    type_income = relationship("TypeIncome", back_populates="incomes")
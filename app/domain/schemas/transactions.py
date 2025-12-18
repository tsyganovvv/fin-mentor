from enum import Enum
from decimal import Decimal
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID


class TransactionsType(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"


class ExpenseCategory(str, Enum):
    FOOD = "food"
    TRANSPORT = "transport"
    UTILITIES = "utilities"
    ENTERTAINMENT = "entertainment"
    SHOPPING = "shopping"
    HEALTH = "health"
    EDUCATION = "education"
    SUBSCRIPTIONS = "subscriptions"
    OTHER_EXPENSE = "other_expense"


class IncomeCategory(str, Enum):
    SALARY = "salary"
    FREELANCE = "freelance"
    INVESTMENTS = "investments"
    GIFT = "gift"   
    BUSINESS = "business" 
    OTHER_INCOME = "other_income"


class TransactionBase(BaseModel):
    amount: Decimal = Field(
        gt=0,
        max_digits=15,
        decimal_places=2,
        description="amount"
    )
    currency: str = Field(
        default="RUB",
        len=3,
        description="currency"
    )
    description: Optional[str] = Field(
        default=None,
        max_length=500,
        description="description"
    )
    category_id: Optional[]
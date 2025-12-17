from fastapi import APIRouter
from .v1.endpoints import transactions

router = APIRouter()

router.include_router(transactions.router, prefix="/v1/transactions", tags=["transactions"])
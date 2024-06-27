from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from internal.receipts.models import Receipt
from wayne_vault.db.session import get_session

router = APIRouter(prefix="/receipts")

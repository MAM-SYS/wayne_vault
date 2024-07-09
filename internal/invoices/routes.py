from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from internal.backpack import InvoiceCreateResponse, TransactionCreateRequest
from internal.invoices import logic
from internal.invoices.models import Invoice
from wayne_vault.db.session import get_session

router = APIRouter(prefix="/invoices")


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_invoice(session: AsyncSession = Depends(get_session)) -> InvoiceCreateResponse:
    invoice: Invoice = await logic.create_invoice(session)
    return InvoiceCreateResponse(id=invoice.id)


@router.post("/{invoice_id}/transactions", status_code=status.HTTP_201_CREATED)
async def add_transaction_to_invoice(invoice_id: str, transaction: TransactionCreateRequest, session:  AsyncSession = Depends(get_session)) -> InvoiceCreateResponse:
    invoice: Invoice = await logic.add_transaction_to_invoice(invoice_id, transaction, session)
    return InvoiceCreateResponse(id=invoice.id)

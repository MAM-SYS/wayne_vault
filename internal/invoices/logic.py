from typing import Optional

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from dev_tools import tracer
from internal.backpack import TransactionCreateRequest
from internal.exceptions import InvoiceNotFoundException, WalletNotFoundException
from internal.invoices.models import Invoice
from internal.transactions.models import Transaction
from internal.wallets.models import Wallet
from internal.shared_logics.wallets import get_or_create_invoice_safe


async def create_invoice(session: AsyncSession) -> Invoice:
    invoice: Invoice = Invoice()
    session.add(invoice)
    await session.flush()
    return invoice


@tracer
async def add_transaction_to_invoice(invoice_id: str, transaction_payload: TransactionCreateRequest, session: AsyncSession) -> Transaction:
    safe_id: Optional[str] = None

    if not (await session.scalar(select(func.count("*")).select_from(Invoice).where(Invoice.id == invoice_id))):
        raise InvoiceNotFoundException()

    if not (await session.scalar(select(func.count("*")).select_from(Wallet).where(Wallet.id == transaction_payload.source_id))):
        raise WalletNotFoundException(wallet_id=transaction_payload.source_id)

    if not (await session.scalar(select(func.count("*")).select_from(Wallet).where(Wallet.id == transaction_payload.target_id))):
        raise WalletNotFoundException(wallet_id=transaction_payload.target_id)

    if transaction_payload.safe_transfer:
        safe_id: str = await get_or_create_invoice_safe(invoice_id=invoice_id, session=session)

    transaction: Transaction = Transaction(
        type=transaction_payload.type,
        amount=transaction_payload.amount,
        source_id=transaction_payload.source_id,
        target_id=transaction_payload.target_id,
        safe_id=safe_id,
        invoice_id=invoice_id
    )

    session.add(transaction)
    await session.flush()
    return transaction

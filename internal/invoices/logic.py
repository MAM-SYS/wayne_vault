from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from dev_tools import tracer
from internal.backpack import TransactionCreateRequest
from internal.exceptions import InvoiceNotFoundException, WalletNotFoundException
from internal.invoices.models import Invoice
from internal.transactions.models import Transaction
from internal.wallets.models import Wallet


async def create_invoice(session: AsyncSession) -> Invoice:
    invoice: Invoice = Invoice()
    session.add(invoice)
    await session.flush()
    return invoice


@tracer
async def add_transaction_to_invoice(invoice_id: str, payload: TransactionCreateRequest, session: AsyncSession) -> Transaction:

    if not (await session.scalar(select(func.count("*")).select_from(Invoice).where(Invoice.id == invoice_id))):
        raise InvoiceNotFoundException()

    if not (await session.scalar(select(func.count("*")).select_from(Wallet).where(Wallet.id == payload.source_id))):
        raise WalletNotFoundException(wallet_id=payload.source_id)

    if not (await session.scalar(select(func.count("*")).select_from(Wallet).where(Wallet.id == payload.target_id))):
        raise WalletNotFoundException(wallet_id=payload.target_id)

    transaction: Transaction = Transaction(
        type=payload.type,
        amount=payload.amount,
        source_id=payload.source_id,
        target_id=payload.target_id,
        invoice_id=invoice_id
    )

    session.add(transaction)
    await session.flush()
    return transaction

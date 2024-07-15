from sqlalchemy import select, update, func, case, or_
from sqlalchemy.ext.asyncio import AsyncSession

from internal.backpack import WalletType
from internal.invoices.models import Invoice
from internal.transactions.models import Transaction
from internal.wallets.models import Wallet


async def get_or_create_invoice_safe(invoice_id: str, session: AsyncSession) -> str:
    safe_id: str
    if safe_id := await session.scalar(select(Invoice.safe_id).where(Invoice.id == invoice_id)):
        return safe_id

    safe: Wallet = Wallet(type=WalletType.Safe)
    session.add(safe)
    await session.flush()
    await session.execute(update(Invoice).where(Invoice.id == invoice_id).values(safe_id=safe.id))
    return safe.id



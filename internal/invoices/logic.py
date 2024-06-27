from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from dev_tools import tracer
from internal.invoices.models import Invoice


async def create_invoice(session: AsyncSession) -> Invoice:
    invoice: Invoice = Invoice()
    session.add(invoice)
    await session.flush()
    return invoice


@tracer
async def add_transaction_to_invoice(invoice_id: str, session: AsyncSession) -> Invoice:
    invoice: Invoice = await session.scalar(select(Invoice).where(Invoice.id == invoice_id))
    print("founded invoice: ", invoice)

from select import select

from sqlalchemy.ext.asyncio import AsyncSession

from internal.wallets.models import Wallet


async def create_wallet(session: AsyncSession) -> Wallet:
    wallet: Wallet = Wallet()
    session.add(wallet)
    await session.flush()
    return wallet

async def get_wallet(wallet_id: str, session: AsyncSession) -> Wallet:
    wallet = await session.scalar(select().where(Wallet.id == wallet_id))


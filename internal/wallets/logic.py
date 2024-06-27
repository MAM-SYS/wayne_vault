from sqlalchemy.ext.asyncio import AsyncSession

from internal.wallets.models import Wallet


async def create_wallet(session: AsyncSession) -> Wallet:
    wallet: Wallet = Wallet()
    session.add(wallet)
    await session.flush()
    return wallet

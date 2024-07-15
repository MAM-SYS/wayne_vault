from sqlalchemy import create_engine, Column, Integer, String, Float, func, case, or_, select


from sqlalchemy.ext.asyncio import AsyncSession

from internal.transactions.models import Transaction
from internal.wallets.models import Wallet


async def create_wallet(session: AsyncSession) -> Wallet:
    wallet: Wallet = Wallet()
    session.add(wallet)
    await session.flush()
    return wallet


async def get_wallet(wallet_id: str, session: AsyncSession) -> Wallet:
    result = await session.execute(
        select(
            func.coalesce(
                func.sum(
                    case(
                        (Transaction.source_id == wallet_id and Transaction.safe_id is None, -1 * Transaction.amount),
                        (Transaction.target_id == wallet_id and Transaction.safe_id is None, Transaction.amount),
                        else_=0
                    )
                ), 0
            ).label('available_amount'),
            func.coalesce(
                func.sum(
                    case(
                        (Transaction.target_id == wallet_id and Transaction.safe_id is not None, -1 * Transaction.amount),
                        (Transaction.source_id == Transaction.safe_id and Transaction.target_id == wallet_id, Transaction.amount),
                        else_=0
                    )
                ), 0
            ).label('blocked_amount')
        ).where(
            or_(
                Transaction.source_id == wallet_id,
                Transaction.target_id == wallet_id,
            ),
        )
    )
    print("*****", list(result))

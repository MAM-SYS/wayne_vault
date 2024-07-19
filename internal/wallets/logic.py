from sqlalchemy import func, case, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from internal.backpack import WalletCreateRequest
from internal.exceptions import WalletAlreadyExistsException
from internal.backpack import WalletType
from internal.transactions.models import Transaction
from internal.wallets.models import Wallet


async def create_wallet(payload: WalletCreateRequest, session: AsyncSession) -> None:
    if await session.scalar(select(func.count("*")).select_from(Wallet).where(Wallet.slug == payload.slug)):
        raise WalletAlreadyExistsException(wallet_slug=payload.slug)

    business_wallet: Wallet = Wallet(type=WalletType.Business, slug=payload.slug)
    safe_wallet: Wallet = Wallet(type=WalletType.Safe, slug=payload.slug)
    session.add_all((business_wallet, safe_wallet))
    await session.flush()


async def get_wallet(wallet_slug: str, session: AsyncSession) -> Wallet:
    # result = await session.execute(
    #     select(
    #         func.coalesce(
    #             func.sum(
    #                 case(
    #                     (Transaction.source_id == wallet_id and Transaction.safe_id is None, -1 * Transaction.amount),
    #                     (Transaction.target_id == wallet_id and Transaction.safe_id is None, Transaction.amount),
    #                     else_=0
    #                 )
    #             ), 0
    #         ).label('available_amount'),
    #         func.coalesce(
    #             func.sum(
    #                 case(
    #                     (Transaction.target_id == wallet_id and Transaction.safe_id is not None,
    #                      -1 * Transaction.amount),
    #                     (Transaction.source_id == Transaction.safe_id and Transaction.target_id == wallet_id,
    #                      Transaction.amount),
    #                     else_=0
    #                 )
    #             ), 0
    #         ).label('blocked_amount')
    #     ).where(
    #         or_(
    #             Transaction.source_id == wallet_id,
    #             Transaction.target_id == wallet_id,
    #         ),
    #     )
    # )
    print("*****", list(result))

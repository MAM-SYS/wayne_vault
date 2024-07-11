from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from internal.wallets import logic
from internal.backpack import WalletCreateResponse
from internal.wallets.models import Wallet
from wayne_vault.db.session import get_session

router = APIRouter(prefix="/wallets")


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_wallet(session: AsyncSession = Depends(get_session)) -> WalletCreateResponse:
    wallet: Wallet = await logic.create_wallet(session)
    return WalletCreateResponse(id=wallet.id)


@router.post("/{wallet_id}", status_code=status.HTTP_200_OK)
async def create_wallet(wallet_id: str, session: AsyncSession = Depends(get_session)) -> WalletCreateResponse:
    wallet: Wallet = await logic.get_wallet(wallet_id, session)
    return WalletCreateResponse(id=wallet.id)


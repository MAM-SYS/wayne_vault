from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from internal.wallets import logic
from internal.backpack import WalletCreateResponse, WalletCreateRequest
from internal.wallets.models import Wallet
from wayne_vault.db.session import get_session

router = APIRouter(prefix="/wallets")


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_wallet(payload: WalletCreateRequest, session: AsyncSession = Depends(get_session)) -> WalletCreateResponse:
    await logic.create_wallet(payload, session)
    return WalletCreateResponse(slug=payload.slug)


@router.get("/{wallet_slug}", status_code=status.HTTP_200_OK)
async def create_wallet(wallet_slug: str, session: AsyncSession = Depends(get_session)) -> WalletCreateResponse:
    wallet: Wallet = await logic.get_wallet(wallet_slug, session)
    return WalletCreateResponse(id=wallet.id, type=wallet.type)


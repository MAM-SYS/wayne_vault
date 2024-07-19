from dataclasses import dataclass

from pydantic import BaseModel

from internal.backpack.enumerations.wallets import WalletType


class WalletCreateRequest(BaseModel):
    slug: str


class WalletCreateResponse(BaseModel):
    slug: str


@dataclass(frozen=True)
class WalletDetails:
    available_amount: int
    blocked_amount: int

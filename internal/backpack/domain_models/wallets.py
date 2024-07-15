from dataclasses import dataclass

from pydantic import BaseModel


class WalletCreateResponse(BaseModel):
    id: str


@dataclass(frozen=True)
class WalletDetails:
    available_amount: int
    blocked_amount: int

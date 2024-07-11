from dataclasses import dataclass


@dataclass(frozen=True)
class WalletDetails:
    available_amount: int
    blocked_amount: int
from pydantic import BaseModel
from internal.backpack.enumerations.transactions import TransactionType


class TransactionCreateRequest(BaseModel):
    amount: int
    type: TransactionType
    schedule: bool
    source_id: str
    target_id: str
    safe_transfer: bool

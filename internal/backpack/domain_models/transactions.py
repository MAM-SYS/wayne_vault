from pydantic import BaseModel

from internal.backpack.enumerations.transactions import TransactionType


class TransactionCreateRequest(BaseModel):
    amount: int
    type: TransactionType
    source_id: str
    target_id: str

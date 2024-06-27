from pydantic import BaseModel


class WalletCreateResponse(BaseModel):
    id: str

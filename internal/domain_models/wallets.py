from pydantic import BaseModel


class WalletCreateResponse(BaseModel):
    id: str

    class Config:
        orm_mode = True

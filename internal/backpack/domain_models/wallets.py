from pydantic import BaseModel, ConfigDict


class WalletCreateResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str

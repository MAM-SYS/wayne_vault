from pydantic import BaseModel


class InvoiceCreateResponse(BaseModel):
    id: str

from pydantic import BaseModel




class InvoiceCreateResponse(BaseModel):
    id: str


class InvoiceItemCreateResponse(BaseModel):
    id: str

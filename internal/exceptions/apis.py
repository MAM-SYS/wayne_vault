from fastapi import status
from fastapi.exceptions import HTTPException


class InvoiceNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Invoice not found."

    def __init__(self) -> None:
        super().__init__(status_code=self.status_code, detail=self.detail)


class WalletNotFoundException(HTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Wallet {wallet_id} not found."

    def __init__(self, wallet_id: str) -> None:
        super().__init__(status_code=self.status_code, detail=self.detail.format(wallet_id=wallet_id))


class WalletAlreadyExistsException(HTTPException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Wallet {wallet_slug} already exists."

    def __init__(self, wallet_slug: str) -> None:
        super().__init__(status_code=self.status_code, detail=self.detail.format(wallet_slug=wallet_slug))

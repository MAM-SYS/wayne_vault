from enum import Enum


class ReceiptType(Enum):
    Deposit = "Deposit"
    Withdraw = "Withdraw"

    def __str__(self):
        return self.value


class ReceiptStatus(Enum):
    Init = "Init"
    Pending = "Pending"
    Accepted = "Accepted"
    Declined = "Declined"
    Canceled = "Canceled"

    def __str__(self):
        return self.value

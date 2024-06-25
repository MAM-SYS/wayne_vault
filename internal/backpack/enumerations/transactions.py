from enum import Enum


class TransactionStatus(Enum):
    Applied = "applied"
    Scheduled = "scheduled"
    Canceled = "canceled"

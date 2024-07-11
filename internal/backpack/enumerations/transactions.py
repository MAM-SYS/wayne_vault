from enum import Enum


class TransactionType(Enum):
    CashIn = "cash_in"
    CashOut = "cash_out"
    Payment = "payment"
    PaymentRefund = "payment_refund"
    Commission = "commission"
    CommissionRefund = "commission_refund"
    # SafeBlock = "safe_block"
    # SafeUnblock = "safe_unblock"


class TransactionStatus(Enum):
    Applied = "applied"
    Scheduled = "scheduled"
    Canceled = "canceled"

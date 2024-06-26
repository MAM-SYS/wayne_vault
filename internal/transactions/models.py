from __future__ import annotations

from datetime import datetime
from typing import Optional

from sqlalchemy import String, func, ForeignKey, INTEGER
from sqlalchemy.dialects.mysql import ENUM
from sqlalchemy.orm import Mapped, mapped_column, relationship

from internal.backpack import TransactionStatus
from internal.backpack.enumerations.transactions import TransactionType
from wayne_vault.db.base import Base
from wayne_vault.db.columns import ulid_gen


class Transaction(Base):
    __tablename__ = 'transactions'

    id: Mapped[str] = mapped_column(String(26), primary_key=True, default=ulid_gen)

    status: Mapped[TransactionStatus] = mapped_column(ENUM(TransactionStatus, name="transaction_status"))
    type: Mapped[TransactionType] = mapped_column(ENUM(TransactionStatus, name="transaction_status"))
    amount: Mapped[int] = mapped_column(INTEGER)

    source_id: Mapped[str] = mapped_column(ForeignKey("wallets.id"))
    source: Mapped["Wallet"] = relationship(foreign_keys=[source_id])

    target_id: Mapped[str] = mapped_column(ForeignKey("wallets.id"))
    target: Mapped["Wallet"] = relationship( foreign_keys=[target_id])

    receipt_id: Mapped[Optional[str]] = mapped_column(ForeignKey("receipts.id"))
    receipt: Mapped[Optional["Receipt"]] = relationship(back_populates="transaction", single_parent=True)

    invoice_item: Mapped[Optional["InvoiceItem"]] = relationship(back_populates="transaction", single_parent=True)

    created_at: Mapped[datetime] = mapped_column(server_default=func.CURRENT_TIMESTAMP())
    updated_at: Mapped[Optional[datetime]] = mapped_column(server_onupdate=func.CURRENT_TIMESTAMP())
    deleted_at: Mapped[Optional[datetime]] = mapped_column()

    def __repr__(self):
        return f"<Transaction {self.id}>"

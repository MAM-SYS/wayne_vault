from __future__ import annotations

from datetime import datetime
from typing import Optional

from sqlalchemy import String, func, ForeignKey, INTEGER, BOOLEAN
from sqlalchemy.dialects.mysql import ENUM
from sqlalchemy.orm import Mapped, mapped_column, relationship

from internal.backpack.enumerations.transactions import TransactionType
from wayne_vault.db.base import Base
from wayne_vault.db.columns import ulid_gen


class Transaction(Base):
    __tablename__ = 'transactions'

    id: Mapped[str] = mapped_column(String(26), primary_key=True, default=ulid_gen)

    type: Mapped[TransactionType] = mapped_column(ENUM(TransactionType, name="transaction_status"))
    safe: Mapped[bool] = mapped_column(BOOLEAN, default=False)
    amount: Mapped[int] = mapped_column(INTEGER)

    source_id: Mapped[str] = mapped_column(ForeignKey("wallets.id"))
    source: Mapped["Wallet"] = relationship(foreign_keys=[source_id])

    safe_id: Mapped[Optional[str]] = mapped_column(ForeignKey("wallets.id"))
    safe: Mapped[Optional["Wallet"]] = relationship(foreign_keys=[safe_id])

    target_id: Mapped[str] = mapped_column(ForeignKey("wallets.id"))
    target: Mapped["Wallet"] = relationship(foreign_keys=[target_id])

    receipt_id: Mapped[Optional[str]] = mapped_column(ForeignKey("receipts.id"))
    receipt: Mapped[Optional["Receipt"]] = relationship(back_populates="transaction", single_parent=True)

    invoice_id: Mapped[str] = mapped_column(ForeignKey("invoices.id"))
    invoice: Mapped["Invoice"] = relationship(back_populates="transactions")

    created_at: Mapped[datetime] = mapped_column(server_default=func.CURRENT_TIMESTAMP())
    updated_at: Mapped[Optional[datetime]] = mapped_column(server_onupdate=func.CURRENT_TIMESTAMP())
    deleted_at: Mapped[Optional[datetime]] = mapped_column()

    def __repr__(self):
        return f"<Transaction {self.id}>"

from __future__ import annotations

from datetime import datetime
from typing import Optional

import ulid
from sqlalchemy import String, func, ForeignKey, INTEGER
from sqlalchemy.dialects.mysql import ENUM
from sqlalchemy.orm import Mapped, mapped_column, relationship

from internal.backpack import TransactionStatus
from wayne_vault.db.base import Base


class Transaction(Base):
    __tablename__ = 'transactions'

    id: Mapped[str] = mapped_column(String(26), primary_key=True, default=ulid.new().str)
    status: Mapped[TransactionStatus] = mapped_column(ENUM(TransactionStatus, name="transaction_status"))
    source_id: Mapped[str] = mapped_column(ForeignKey("wallets.id"))
    source: Mapped["Wallet"] = relationship(back_populates="outgoing_transactions")
    target_id: Mapped[str] = mapped_column(ForeignKey("wallets.id"))
    target: Mapped["Wallet"] = relationship(back_populates="incoming_transactions")
    amount: Mapped[int] = mapped_column(INTEGER)
    created_at: Mapped[datetime] = mapped_column(server_default=func.CURRENT_TIMESTAMP())
    updated_at: Mapped[Optional[datetime]] = mapped_column(server_onupdate=func.CURRENT_TIMESTAMP())
    deleted_at: Mapped[Optional[datetime]] = mapped_column()

    def __repr__(self):
        return f"<Transaction {self.id}>"

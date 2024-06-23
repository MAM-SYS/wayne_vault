from __future__ import annotations

from datetime import datetime


import ulid
from sqlalchemy import String, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from wayne_vault.db.base import Base


class Invoice(Base):
    __tablename__ = 'invoices'

    id: Mapped[str] = mapped_column(String(26), primary_key=True, default=ulid.new().str)
    source_id: Mapped[str] = mapped_column(ForeignKey("wallets.id"), nullable=False)
    source: Mapped["Wallet"] = relationship(back_populates="outgoing_transactions")
    target_id: Mapped[str] = mapped_column(ForeignKey("wallets.id"), nullable=False, )
    target: Mapped["Wallet"] = relationship(back_populates="incoming_transactions")
    amount: Mapped[int] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(nullable=False, server_default=func.CURRENT_TIMESTAMP())
    updated_at: Mapped[datetime] = mapped_column(nullable=True, server_onupdate=func.CURRENT_TIMESTAMP())

    def __repr__(self):
        return f"<Transaction {self.id}>"

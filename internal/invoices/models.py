from __future__ import annotations

from datetime import datetime
from typing import Optional

import ulid
from sqlalchemy import String, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from wayne_vault.db.base import Base


class Invoice(Base):
    __tablename__ = 'invoices'

    id: Mapped[str] = mapped_column(String(26), primary_key=True, default=ulid.new().str)
    items: Mapped[Optional["InvoiceItem"]] = relationship("InvoiceItem", back_populates="invoice")
    created_at: Mapped[datetime] = mapped_column(server_default=func.CURRENT_TIMESTAMP())
    updated_at: Mapped[datetime] = mapped_column(server_onupdate=func.CURRENT_TIMESTAMP())
    deleted_at: Mapped[Optional[datetime]] = mapped_column()

    def __repr__(self):
        return f"<Invoice {self.id}>"


class InvoiceItem(Base):
    __tablename__ = 'invoice_items'

    id: Mapped[str] = mapped_column(String(26), primary_key=True, default=ulid.new().str)
    invoice_id: Mapped[str] = mapped_column(ForeignKey("invoices.id"))
    invoice: Mapped["Invoice"] = relationship(back_populates="items")
    receipt_id: Mapped[Optional[str]] = mapped_column(ForeignKey("receipts.id"))
    receipt: Mapped[Optional["Receipt"]] = relationship(back_populates="invoice_item", single_parent=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.CURRENT_TIMESTAMP())
    updated_at: Mapped[Optional[datetime]] = mapped_column(server_onupdate=func.CURRENT_TIMESTAMP())
    deleted_at: Mapped[Optional[datetime]] = mapped_column()

    def __repr__(self):
        return f"<InvoiceItem {self.id}>"


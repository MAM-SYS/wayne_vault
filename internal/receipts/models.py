from __future__ import annotations

from datetime import datetime
from typing import Optional, Dict

from sqlalchemy import String
from sqlalchemy import func
from sqlalchemy.dialects.mysql import ENUM, JSON
from sqlalchemy.orm import Mapped, mapped_column

from internal.backpack import ReceiptType, ReceiptStatus
from wayne_vault.db.base import Base
from wayne_vault.db.columns import ulid_gen


class Receipt(Base):
    __tablename__ = 'receipts'
    id: Mapped[str] = mapped_column(String(26), primary_key=True, default=ulid_gen)
    type: Mapped[ReceiptType] = mapped_column(ENUM(ReceiptType, name="receipt_type"))
    status: Mapped[ReceiptStatus] = mapped_column(ENUM(ReceiptStatus, name="receipt_status"))
    meta: Mapped[Optional[Dict]] = mapped_column(JSON)
    created_at: Mapped[datetime] = mapped_column(server_default=func.CURRENT_TIMESTAMP())
    updated_at: Mapped[Optional[datetime]] = mapped_column(server_onupdate=func.CURRENT_TIMESTAMP())
    deleted_at: Mapped[Optional[datetime]] = mapped_column()

    def __repr__(self):
        return f"<Receipt {self.id}>"

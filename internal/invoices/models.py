from __future__ import annotations

from datetime import datetime
from typing import Optional, List

from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from wayne_vault.db.base import Base
from wayne_vault.db.columns import ulid_gen


class Invoice(Base):
    __tablename__ = 'invoices'

    id: Mapped[str] = mapped_column(String(26), primary_key=True, default=ulid_gen)

    transactions: Mapped[Optional[List["Transaction"]]] = relationship(back_populates="invoice")

    created_at: Mapped[datetime] = mapped_column(server_default=func.CURRENT_TIMESTAMP())
    updated_at: Mapped[Optional[datetime]] = mapped_column(server_onupdate=func.CURRENT_TIMESTAMP())
    deleted_at: Mapped[Optional[datetime]] = mapped_column()

    def __repr__(self):
        return f"<Invoice {self.id}>"

from datetime import datetime

import ulid
from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column

from wayne_vault.db.base import Base


class Wallet(Base):
    __tablename__ = 'wallets'

    id: Mapped[str] = mapped_column(String(26), primary_key=True, default=ulid.new().str)
    available_amount: Mapped[int] = mapped_column(nullable=False, default=0)
    blocked_amount: Mapped[int] = mapped_column(nullable=False, default=0)
    created_at: Mapped[datetime] = mapped_column(nullable=False, server_default=func.CURRENT_TIMESTAMP())
    updated_at: Mapped[datetime] = mapped_column(nullable=True, server_onupdate=func.CURRENT_TIMESTAMP())

    def __repr__(self):
        return f"<Wallet {self.id}>"

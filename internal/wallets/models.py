from datetime import datetime
from typing import Optional

from sqlalchemy import String, func
from sqlalchemy.dialects.mysql import ENUM
from sqlalchemy.orm import Mapped, mapped_column, relationship

from internal.backpack import WalletType
from wayne_vault.db.base import Base
from wayne_vault.db.columns import ulid_gen


class Wallet(Base):
    __tablename__ = 'wallets'

    id: Mapped[str] = mapped_column(String(26), primary_key=True, default=ulid_gen)
    type: Mapped[WalletType] = mapped_column(ENUM(WalletType, name="wallet_type"), default=WalletType.Business)

    invoice: Mapped[Optional["Invoice"]] = relationship(back_populates="safe")

    created_at: Mapped[datetime] = mapped_column(nullable=False, server_default=func.CURRENT_TIMESTAMP())
    updated_at: Mapped[Optional[datetime]] = mapped_column(server_onupdate=func.CURRENT_TIMESTAMP())
    deleted_at: Mapped[Optional[datetime]] = mapped_column()

    def __repr__(self):
        return f"<Wallet {self.id}>"

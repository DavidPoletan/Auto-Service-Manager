from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import String, Integer, Numeric, DateTime, ForeignKey, CheckConstraint, func
from backend.app.database import Base
from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .workorderparts import WorkOrderParts

class Part(Base):
    __tablename__ =  "parts"
    __table_args__ = (CheckConstraint("unit_price > 0", name="ck_unit_price"))

    id:                Mapped[int] =        mapped_column(Integer, primary_key=True, autoincrement=True)
    name:              Mapped[str] =        mapped_column(String(100))
    manufacturer:      Mapped[str | None] = mapped_column(String(100))
    part_number:       Mapped[str | None] = mapped_column(String(50))
    unit_price:        Mapped[Decimal] =    mapped_column(Numeric(18,2))
    quantity_in_stock: Mapped[int] =        mapped_column(Integer)
    minimum_stock:     Mapped[int | None] = mapped_column(Integer)
    created_at:        Mapped[datetime] =   mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at:        Mapped[datetime] =   mapped_column(DateTime(timezone=True))

    workorderparts: Mapped[list["WorkOrderParts"]] = relationship(back_populates="parts")
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import Integer, Numeric, DateTime, ForeignKey, CheckConstraint, func
from sqlalchemy import Enum as SQLEnum
from backend.app.database import Base
from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING
from enums import InvoiceStatus, InvoiceMethod

if TYPE_CHECKING:
    from .workorder import WorkOrder

class Invoice(Base):
    __tablename__ = "invoices"
    __table_args__ = (CheckConstraint("total_price > 0", name="ck_total_price"))

    id:             Mapped[int] =           mapped_column(Integer, primary_key=True, autoincrement=True)
    workorder_id:   Mapped[int] =           mapped_column(Integer, ForeignKey("workorders.id"))
    issue_date:     Mapped[datetime] =      mapped_column(DateTime(timezone=True), server_default=func.now())
    total_price:    Mapped[Decimal] =       mapped_column(Numeric(18,2))
    payment_status: Mapped[InvoiceStatus] = mapped_column(SQLEnum(InvoiceStatus), name="payment_status")
    payment_method: Mapped[InvoiceMethod] = mapped_column(SQLEnum(InvoiceMethod), name="payment_method")
    created_at:     Mapped[datetime] =      mapped_column(DateTime(timezone=True), server_default=func.now())

    workorders: Mapped[list["WorkOrder"]] = relationship(back_populates="invoices")
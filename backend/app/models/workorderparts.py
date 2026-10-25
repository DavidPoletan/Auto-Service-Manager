from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import Integer, ForeignKey, CheckConstraint
from backend.app.database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .workorder import WorkOrder
    from .part import Part

class WorkOrderParts(Base):
    __tablename__ =  "workorderparts"
    __table_args__ = (CheckConstraint("quantity > 0", name="ck_used_quantity"))

    workorder_id: Mapped[int] = mapped_column(Integer, ForeignKey("workorders.id"), nullable=False)
    part_id:      Mapped[int] = mapped_column(Integer, ForeignKey("parts.id"), nullable=False)
    quantity:     Mapped[int] = mapped_column(Integer, nullable=False)

    workorders: Mapped[list["WorkOrder"]] = relationship(back_populates="workorderparts")
    parts:      Mapped[list["Part"]] =      relationship(back_populates="workorderparts")
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import Integer, Text, Numeric, DateTime, ForeignKey, CheckConstraint, func
from sqlalchemy import Enum as SQLEnum
from backend.app.database import Base
from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING
from enums import WorkOrderStatus

if TYPE_CHECKING:
    from .user import User
    from .appointment import Appointment
    from .workorderparts import WorkOrderParts

class WorkOrder(Base):
    __tablename__ =  "workorders"
    __table_args__ = (CheckConstraint("labor_cost > 0", name="ck_labor_cost"))

    id:                  Mapped[int] =             mapped_column(Integer, primary_key=True, autoincrement=True)
    appointment_id:      Mapped[int] =             mapped_column(Integer, ForeignKey("appointments.id"))
    mechanic_id:         Mapped[int | None] =      mapped_column(Integer, ForeignKey("users.id"))
    problem_description: Mapped[str] =             mapped_column(Text)
    labor_cost:          Mapped[Decimal] =         mapped_column(Numeric(18,2))
    status:              Mapped[WorkOrderStatus] = mapped_column(SQLEnum(WorkOrderStatus), name="workorder_status")
    odometer:            Mapped[int | None] =      mapped_column(Integer)
    diagnosis:           Mapped[str | None] =      mapped_column(Text)
    work_performed:      Mapped[str | None] =      mapped_column(Text)
    recommendations:     Mapped[str | None] =      mapped_column(Text)
    opened_at:           Mapped[datetime] =        mapped_column(DateTime(timezone=True), server_default=func.now())
    completed_at:        Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_at:          Mapped[datetime] =        mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at:          Mapped[datetime | None] = mapped_column(DateTime(timezone=True))

    users:          Mapped[list["User"]] =           relationship(back_populates="workorders")
    appointments:   Mapped[list["Appointment"]] =    relationship(back_populates="workorders")
    workorderparts: Mapped[list["WorkOrderParts"]] = relationship(back_populates="workorders")
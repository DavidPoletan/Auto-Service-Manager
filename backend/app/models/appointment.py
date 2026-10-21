from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import Integer, Text, DateTime, ForeignKey, func
from sqlalchemy import Enum as SQLEnum
from backend.app.database import Base
from datetime import datetime
from typing import TYPE_CHECKING
from enums import AppointmentStatus

if TYPE_CHECKING:
    from .car import Car

class Appointment(Base):
    __tablename__ = "appointments"

    id:               Mapped[int] =               mapped_column(Integer, primary_key=True, autoincrement=True)
    car_id:           Mapped[int] =               mapped_column(Integer, ForeignKey("cars.id"))
    appointment_date: Mapped[datetime] =          mapped_column(DateTime(timezone=True))
    status:           Mapped[AppointmentStatus] = mapped_column(SQLEnum(AppointmentStatus), name="appointment_status")
    notes:            Mapped[str | None] =        mapped_column(Text)
    created_at:       Mapped[datetime] =          mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at:       Mapped[datetime | None] =   mapped_column(DateTime(timezone=True))

    cars: Mapped[list["Car"]] = relationship(back_populates="appointments")
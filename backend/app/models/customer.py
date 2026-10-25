from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import String, Integer, Text, DateTime, func
from backend.app.database import Base
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .car import Car

class Customer(Base):
    __tablename__ = "customers"

    id:         Mapped[int] =             mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    first_name: Mapped[str] =             mapped_column(String(50), nullable=False)
    last_name:  Mapped[str] =             mapped_column(String(50), nullable=False)
    phone:      Mapped[str | None] =      mapped_column(String(30))
    email:      Mapped[str | None] =      mapped_column(String(255))
    address:    Mapped[str | None] =      mapped_column(Text)
    created_at: Mapped[datetime] =        mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))

    cars: Mapped[list["Car"]] = relationship(back_populates="customers")
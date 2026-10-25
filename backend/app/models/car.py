from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import String, Integer, DateTime, ForeignKey, CheckConstraint, func
from backend.app.database import Base
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .customer import Customer

class Car(Base):
    __tablename__ =  "cars"
    __table_args__ = (CheckConstraint("year >= 1900 AND year <= 2027", name="ck_cars_year_range"))

    id:                  Mapped[int] =             mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    customer_id:         Mapped[int] =             mapped_column(Integer, ForeignKey("customers.id"), nullable=False)
    brand:               Mapped[str] =             mapped_column(String(50), nullable=False)
    model:               Mapped[str] =             mapped_column(String(50), nullable=False)
    year:                Mapped[int] =             mapped_column(Integer, nullable=False)
    vin:                 Mapped[str | None] =      mapped_column(String(17))
    registration_number: Mapped[str | None] =      mapped_column(String(20))
    color:               Mapped[str | None] =      mapped_column(String(30))
    mileage:             Mapped[int | None] =      mapped_column(Integer)
    fuel_type:           Mapped[str | None] =      mapped_column(String(20))
    transmission:        Mapped[str | None] =      mapped_column(String(20))
    created_at:          Mapped[datetime] =        mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at:          Mapped[datetime | None] = mapped_column(DateTime(timezone=True))

    customer: Mapped["Customer"] = relationship(back_populates="cars")
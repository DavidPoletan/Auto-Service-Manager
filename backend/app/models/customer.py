from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Text, DateTime, func
from backend.app.database import Base
from datetime import datetime

class Customer(Base):
    __tablename__ = "customers"

    id:         Mapped[int] =             mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] =             mapped_column(String(50))
    last_name:  Mapped[str] =             mapped_column(String(50))
    phone:      Mapped[str | None] =      mapped_column(String(30))
    email:      Mapped[str | None] =      mapped_column(String(255))
    address:    Mapped[str | None] =      mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] =        mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
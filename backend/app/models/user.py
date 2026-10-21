from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import String, Integer, Text, Boolean, DateTime, func
from sqlalchemy import Enum as SQLEnum
from backend.app.database import Base
from datetime import datetime
from typing import TYPE_CHECKING
from enums import UserRole

if TYPE_CHECKING:
    from .workorder import WorkOrder

class User(Base):
    __tablename__ = "users"

    id:            Mapped[int] =             mapped_column(Integer, primary_key=True, autoincrement=True)
    username:      Mapped[str] =             mapped_column(String(50))
    email:         Mapped[str] =             mapped_column(String(255))
    password_hash: Mapped[str] =             mapped_column(Text)
    first_name:    Mapped[str] =             mapped_column(String(50))
    last_name:     Mapped[str] =             mapped_column(String(50))
    role:          Mapped[UserRole] =        mapped_column(SQLEnum(UserRole), name="user_role")
    active:        Mapped[bool] =            mapped_column(Boolean, default=True)
    created_at:    Mapped[datetime] =        mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at:    Mapped[datetime | None] = mapped_column(DateTime(timezone=True))

    workorders: Mapped[list["WorkOrder"]] = relationship(back_populates="users")
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

    id:            Mapped[int] =             mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    username:      Mapped[str] =             mapped_column(String(50),  nullable=False)
    email:         Mapped[str] =             mapped_column(String(255), nullable=False)
    password_hash: Mapped[str] =             mapped_column(Text, nullable=False)
    first_name:    Mapped[str] =             mapped_column(String(50), nullable=False)
    last_name:     Mapped[str] =             mapped_column(String(50), nullable=False)
    role:          Mapped[UserRole] =        mapped_column(SQLEnum(UserRole), name="user_role", nullable=False)
    active:        Mapped[bool] =            mapped_column(Boolean, default=True, nullable=False)
    created_at:    Mapped[datetime] =        mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at:    Mapped[datetime | None] = mapped_column(DateTime(timezone=True))

    workorders: Mapped[list["WorkOrder"]] = relationship(back_populates="users")
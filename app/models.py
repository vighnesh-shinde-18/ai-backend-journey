from uuid import UUID
from sqlalchemy import String, Integer, Uuid
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class User(Base):
    __tablename__ = "users"

    # Enforcing native_uuid=False ensures SQLAlchemy formats UUID strings uniformly inside SQLite
    id: Mapped[UUID] = mapped_column(Uuid(native_uuid=False), primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)

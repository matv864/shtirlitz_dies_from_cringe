import uuid

from sqlalchemy.orm import Mapped, mapped_column

from src.database.core import Base


class Auth(Base):
    __tablename__ = "auth"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    username: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)

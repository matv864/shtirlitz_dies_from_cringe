from datetime import date
from typing import List
import uuid

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.core import Base


class Card(Base):
    __tablename__ = "card"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    pet_name: Mapped[str] = mapped_column()
    pet_type_id: Mapped[int] = mapped_column(ForeignKey("pet_type.id"))
    date_birth: Mapped[date] = mapped_column(DateTime(timezone=True))
    main_image: Mapped[str] = mapped_column(nullable=True)
    castrated: Mapped[bool] = mapped_column(default=False)
    vaccinated: Mapped[bool] = mapped_column(default=False)
    cat_litter_box: Mapped[bool] = mapped_column(default=False)
    description: Mapped[str] = mapped_column(nullable=True)
    counter_views: Mapped[int] = mapped_column(default=0)
    donated_amount: Mapped[int] = mapped_column(default=0)

    pet_type: Mapped["Pet_type"] = relationship()
    articles: Mapped[List["Article"]] = relationship()


class Article(Base):
    __tablename__ = "article"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(nullable=False)
    body: Mapped[str] = mapped_column()
    date_publish: Mapped[date] = mapped_column(
        DateTime(timezone=True), nullable=False)
    card_id: Mapped[int] = mapped_column(ForeignKey("card.id"))

    images: Mapped[List["Image"]] = relationship()


class Pet_type(Base):
    __tablename__ = "pet_type"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)


class Image(Base):
    __tablename__ = "image"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    filename: Mapped[str] = mapped_column(nullable=False)
    article_id: Mapped[int] = mapped_column(ForeignKey("article.id"))

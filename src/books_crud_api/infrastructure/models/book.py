from datetime import datetime
from sqlalchemy import DateTime, Integer, String, func
from books_crud_api.infrastructure.db import Base
from sqlalchemy.orm import Mapped, mapped_column


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(
        name="id", type_=Integer, primary_key=True, index=True
    )
    title: Mapped[str] = mapped_column(name="title", type_=String(100), nullable=False)
    author: Mapped[str] = mapped_column(
        name="author", type_=String(100), nullable=False
    )
    published_year: Mapped[int] = mapped_column(
        name="published_year", type_=Integer, nullable=False
    )
    created_on: Mapped[datetime] = mapped_column(
        name="created_on", type_=DateTime(timezone=False), server_default=func.now()
    )

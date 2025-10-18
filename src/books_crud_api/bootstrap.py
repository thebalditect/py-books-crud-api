from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from books_crud_api.domain.repositories.abstract_book_repository import (
    AbstractBookRepository,
)
from books_crud_api.infrastructure.db import get_db
from books_crud_api.infrastructure.repositories.sqlalchemy_book_repository import (
    SqlAlchemyBookRepository,
)


def get_book_repository(
    session: AsyncSession = Depends(get_db),
) -> AbstractBookRepository:
    repository = SqlAlchemyBookRepository(session)
    return repository

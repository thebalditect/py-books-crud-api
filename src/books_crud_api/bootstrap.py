from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from books_crud_api.domain.repositories.abstract_book_repository import (
    AbstractBookRepository,
)
from books_crud_api.infrastructure.db import get_db
from books_crud_api.infrastructure.repositories.sqlalchemy_book_repository import (
    SqlAlchemyBookRepository,
)
from books_crud_api.use_cases.add_book.handler import AddBookCommandHandler
from books_crud_api.use_cases.delete_book.handler import DeleteBookCommandHandler
from books_crud_api.use_cases.get_book.handler import GetBookQueryHandler
from books_crud_api.use_cases.update_book.handler import UpdateBookCommandHandler


def get_book_repository(
    session: AsyncSession = Depends(get_db),
) -> AbstractBookRepository:
    repository = SqlAlchemyBookRepository(session)
    return repository


def get_add_book_handler(
    repository: AbstractBookRepository = Depends(get_book_repository),
) -> AddBookCommandHandler:
    return AddBookCommandHandler(repository=repository)


def get_get_book_handler(
    repository: AbstractBookRepository = Depends(get_book_repository),
) -> GetBookQueryHandler:
    return GetBookQueryHandler(repository=repository)


def get_update_book_handler(
    repository: AbstractBookRepository = Depends(get_book_repository),
) -> UpdateBookCommandHandler:
    return UpdateBookCommandHandler(repository=repository)


def get_delete_book_handler(
    repository: AbstractBookRepository = Depends(get_book_repository),
) -> DeleteBookCommandHandler:
    return DeleteBookCommandHandler(repository=repository)

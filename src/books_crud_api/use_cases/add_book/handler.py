from books_crud_api.domain.entities.book import Book
from books_crud_api.domain.entities.common.result import Result
from books_crud_api.domain.repositories.abstract_book_repository import (
    AbstractBookRepository,
)
from books_crud_api.use_cases.add_book.command import AddBookCommand


class AddBookCommandHandler:

    def __init__(self, repository: AbstractBookRepository) -> None:
        self.repository = repository

    async def handle(self, command: AddBookCommand) -> Result[None]:
        book = Book(
            id=None,
            title=command.title,
            author=command.author,
            published_year=command.published_year,
            created_on=None,
        )
        result = await self.repository.add(book=book)
        return result

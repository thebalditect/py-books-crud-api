from books_crud_api.domain.entities.book import Book
from books_crud_api.domain.repositories.abstract_book_repository import (
    AbstractBookRepository,
)
from books_crud_api.use_cases.update_book.command import UpdateBookCommand


class UpdateBookCommandHandler:
    def __init__(self, repository: AbstractBookRepository) -> None:
        self.repository = repository

    async def handle(self, id: int, command: UpdateBookCommand) -> None:

        to_be_updated_book = Book(
            id=id,
            title=command.title,
            author=command.author,
            published_year=command.published_year,
            created_on=None,
        )

        await self.repository.update(id, to_be_updated_book)

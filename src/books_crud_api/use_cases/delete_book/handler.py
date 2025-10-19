from books_crud_api.domain.entities.common.result import Result
from books_crud_api.domain.repositories.abstract_book_repository import (
    AbstractBookRepository,
)


class DeleteBookCommandHandler:

    def __init__(self, repository: AbstractBookRepository) -> None:
        self.repository = repository

    async def handle(self, id: int) -> Result[None]:
        return await self.repository.delete(id)

from books_crud_api.domain.repositories.abstract_book_repository import (
    AbstractBookRepository,
)


class DeleteBookCommandHandler:

    def __init__(self, repository: AbstractBookRepository) -> None:
        self.repository = repository

    async def handle(self, id: int) -> None:
        retrieved_book = await self.repository.get_by_id(id)

        if retrieved_book is None:
            return None

        await self.repository.delete(id)

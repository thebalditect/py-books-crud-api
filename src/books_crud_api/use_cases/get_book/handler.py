from books_crud_api.domain.repositories.abstract_book_repository import (
    AbstractBookRepository,
)
from books_crud_api.use_cases.get_book.response import GetBookQueryResponse


class GetBookQueryHandler:

    def __init__(self, repository: AbstractBookRepository) -> None:
        self.repository = repository

    async def handle(self, id: int) -> GetBookQueryResponse | None:

        book = await self.repository.get_by_id(id=id)

        if book is None:
            return None

        query_response = GetBookQueryResponse(
            id=book.id,
            title=book.title,
            author=book.author,
            published_year=book.published_year,
            created_on=book.created_on,
        )
        return query_response

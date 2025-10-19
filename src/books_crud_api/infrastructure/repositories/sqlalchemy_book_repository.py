from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from books_crud_api.domain.entities.book import Book as BookEntity
from books_crud_api.domain.entities.book_errors import BookErrors
from books_crud_api.domain.entities.common.result import Result
from books_crud_api.domain.repositories.abstract_book_repository import (
    AbstractBookRepository,
)
from books_crud_api.infrastructure.models.book import Book as BookModel


class SqlAlchemyBookRepository(AbstractBookRepository):

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def add(self, book: BookEntity) -> Result[None]:

        book_model = BookModel(
            title=book.title, author=book.author, published_year=book.published_year
        )
        self.session.add(book_model)
        await self.session.commit()
        return Result[None].success(None)

    async def get_by_id(self, id: int) -> Result[BookEntity]:
        result = await self.session.execute(select(BookModel).where(BookModel.id == id))
        book_model = result.scalar_one_or_none()

        if book_model is None:
            return Result[BookEntity].failure(BookErrors.not_found(id=id))

        book_entity = BookEntity(
            id=book_model.id,
            title=book_model.title,
            author=book_model.author,
            published_year=book_model.published_year,
            created_on=book_model.created_on,
        )
        return Result[BookEntity].success(book_entity)

    async def update(self, id: int, book: BookEntity) -> Result[None]:

        book_retrieval_result = await self.get_by_id(id)

        if book_retrieval_result.is_failure:
            return Result[None].failure(BookErrors.not_found(id=id))

        await self.session.execute(
            update(BookModel).where(BookModel.id == id).values(**book.__dict__)
        )
        await self.session.commit()
        return Result[None].success(None)

    async def delete(self, id: int) -> Result[None]:
        book_retrieval_result = await self.get_by_id(id)

        if book_retrieval_result.is_failure:
            return Result[None].failure(BookErrors.not_found(id=id))

        await self.session.execute(delete(BookModel).where(BookModel.id == id))
        await self.session.commit()
        return Result[None].success(None)

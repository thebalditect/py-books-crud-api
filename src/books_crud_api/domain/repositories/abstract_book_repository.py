from abc import ABC, abstractmethod

from books_crud_api.domain.entities.book import Book
from books_crud_api.domain.entities.common.result import Result


class AbstractBookRepository(ABC):

    @abstractmethod
    async def add(self, book: Book) -> Result[None]:
        pass

    @abstractmethod
    async def get_by_id(self, id: int) -> Result[Book]:
        pass

    @abstractmethod
    async def update(self, id: int, book: Book) -> Result[None]:
        pass

    @abstractmethod
    async def delete(self, id: int) -> Result[None]:
        pass

from abc import ABC, abstractmethod

from books_crud_api.domain.entities.book import Book


class AbstractBookRepository(ABC):

    @abstractmethod
    async def add(self, book: Book) -> None:
        pass

    @abstractmethod
    async def get_by_id(self, id: int) -> Book:
        pass

    @abstractmethod
    async def update(self, id: int, book: Book) -> None:
        pass

    @abstractmethod
    async def delete(self, id: int) -> None:
        pass

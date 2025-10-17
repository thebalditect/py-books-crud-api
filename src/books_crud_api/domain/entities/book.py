from datetime import datetime


class Book:
    def __init__(
        self, title: str, author: str, published_year: int, created_on: datetime | None
    ) -> None:
        self.title = title
        self.author = author
        self.published_year = published_year
        self.created_on = created_on

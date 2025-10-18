from datetime import datetime


class GetBookQueryResponse:
    def __init__(
        self,
        id: int | None,
        title: str,
        author: str,
        published_year: int,
        created_on: datetime | None,
    ) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.published_year = published_year
        self.created_on = created_on

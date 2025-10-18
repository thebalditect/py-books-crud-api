class UpdateBookCommand:
    def __init__(self, title: str, author: str, published_year: int):
        self.title = title
        self.author = author
        self.published_year = published_year

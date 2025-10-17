from pydantic import BaseModel, Field


class AddBookCommand(BaseModel):
    title: str = Field(..., max_length=100, min_length=5)
    author: str = Field(..., max_length=100, min_length=5)
    published_year: int = Field(...)

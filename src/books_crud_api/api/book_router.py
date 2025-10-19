from fastapi import APIRouter, Depends

from books_crud_api.bootstrap import get_add_book_handler, get_get_book_handler
from books_crud_api.use_cases.add_book.command import AddBookCommand
from books_crud_api.use_cases.add_book.handler import AddBookCommandHandler
from books_crud_api.use_cases.get_book.handler import GetBookQueryHandler
from books_crud_api.use_cases.get_book.response import GetBookQueryResponse

router = APIRouter(prefix="/books")


@router.post("/", status_code=201)
async def add_book(
    command: AddBookCommand,
    handler: AddBookCommandHandler = Depends(get_add_book_handler),
) -> None:

    await handler.handle(command)


@router.get("/{id}", response_model=GetBookQueryResponse, status_code=200)
async def get_book(
    id: int, handler: GetBookQueryHandler = Depends(get_get_book_handler)
) -> GetBookQueryResponse | None:
    result = await handler.handle(id=id)

    if result.is_failure:
        return None

    return result.value

from fastapi import FastAPI

from books_crud_api.api.book_router import router


app = FastAPI(title="Book Crud API")
app.include_router(router=router)

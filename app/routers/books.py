from fastapi import APIRouter, status
from ..database.book_crud import BookBase, BookDB
from ..database import book_crud

router = APIRouter(prefix="/books")

@router.get("/", response_model=list[BookDB])
def get_books(author: str = ""):
    return book_crud.get_books(author)

@router.get("/{id}", response_model=BookDB)
def get_book(id: int):
    return book_crud.get_book(id)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_book(book_in: BookBase):
    return book_crud.create_book(book_in)

@router.delete("/{id}")
def delete_book(id: int):
    return book_crud.delete_book(id)


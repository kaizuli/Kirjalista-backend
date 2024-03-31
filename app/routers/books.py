from fastapi import APIRouter, status, Depends
from sqlmodel import Session
from ..database.models import BookBase, BookDB, BookCreate
from ..database import book_crud
from ..database.database import get_session

router = APIRouter(prefix="/books")

@router.get("/", response_model=list[BookDB])
def get_books(*, session: Session = Depends(get_session), author: str = ""):
    books = book_crud.get_books(session)
    return books

@router.get("/{id}", response_model=BookDB)
def get_book(*, session: Session = Depends(get_session), id: int):
    return book_crud.get_book(session, id)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_book(*, session: Session = Depends(get_session), book_in: BookCreate):
    book = book_crud.create_book(session, book_in)
    return book

@router.delete("/{id}")
def delete_book(*, session: Session = Depends(get_session), id: int):
    return book_crud.delete_book(session, id)


from fastapi import HTTPException
from .models import BookBase, BookDB, BookCreate
from sqlmodel import Session, select


def get_books(session: Session):
    return session.exec(session(BookDB)).all()

def get_book(session: Session, id: int):
    book = session.get(BookDB, id)
    if not book:
        raise HTTPException(status_code=404, detail=f"Book with id {id} not found.")
    return book

def create_book(session: Session, book_in: BookCreate):
    bookdb = BookDB.model_validate(book_in)
    session.add(bookdb)
    session.commit()
    session.refresh(bookdb)
    return bookdb

def delete_book(session: Session, id: int):
    book = session.get(BookDB, int)
    if not book:
        raise HTTPException(status_code=404, detail=f"Book with id {id} not found.")
    session.delete(book)
    session.commit()
    return {"message": f"Book with id {id} deleted"}

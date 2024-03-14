from fastapi import HTTPException
from .models import AuthorBase, AuthorDB
from sqlmodel import Session, select

authors = {
    0: {"id": 0, "name": "Adrzej Sapkowski"},
    1: {"id": 1, "name": "Ursula K. Le Guin"},
    2: {"id": 2, "name": "Diana Wynne Jones"}
}

def get_authors(session: Session):
    return session.exec(session(AuthorDB)).all()

def get_author(session: Session, id: int):
    author = session.get(AuthorDB, id)
    if not author:
        raise HTTPException(status_code=404, detail=f"Author with id {id} not found.")
    return author

def save_author(session: Session, author_in: AuthorBase):
    author_db = AuthorDB.model_validate(author_in)
    session.add(author_db)
    session.commit()
    session.refresh(author_db)
    return author_db

def delete_author(session: Session, id: int):
    author = session.get(AuthorDB, id)
    if not author:
        raise HTTPException(status_code=404, detail=f"Author with id {id} not found.")
    session.delete(author)
    session.commit()
    return {"message": f"Author with id {id} deleted"}


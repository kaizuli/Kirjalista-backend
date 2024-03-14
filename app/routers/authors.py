from fastapi import APIRouter, status, Depends
from sqlmodel import Session
from ..database.models import AuthorBase, AuthorDB
from ..database import author_crud
from ..database.database import get_session

router = APIRouter(prefix="/authors")

@router.get("/", response_model=list[AuthorDB])
def get_authors(*, session: Session = Depends(get_session)):
    return author_crud.get_authors(session)

@router.get("/{id}", response_model=AuthorDB)
def get_author(*, session: Session = Depends(get_session), id: int):
    return author_crud.get_author(session, id)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_author(*, session: Session = Depends(get_session), author_in: AuthorBase):
    return author_crud.save_author(session, author_in)

@router.delete("/{id}")
def remove_author(*, session: Session = Depends(get_session), id: int):
    return author_crud.delete_author(session, id)

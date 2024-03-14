from fastapi import APIRouter, status
from ..database.author_crud import (
    fetch_author,
    fetch_authors,
    save_author,
    delete_author
)
from ..database.models import AuthorBase, AuthorDB

router = APIRouter(prefix="/authors")

@router.get("/", response_model=list[AuthorDB])
def get_authors():
    return fetch_authors()

@router.get("/{id}", response_model=AuthorDB)
def get_author(id: int):
    return fetch_author(id)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_author(author_in: AuthorBase):
    return save_author(author_in)

@router.delete("/{id}")
def remove_author(id: int):
    return delete_author(id)

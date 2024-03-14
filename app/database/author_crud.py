from fastapi import HTTPException
from .models import AuthorBase, AuthorDB

authors = {
    0: {"id": 0, "name": "Adrzej Sapkowski"},
    1: {"id": 1, "name": "Ursula K. Le Guin"},
    2: {"id": 2, "name": "Diana Wynne Jones"}
}

def fetch_authors():
    return [authors[a] for a in authors]


def fetch_author(id: int):
    if id not in authors:
        raise HTTPException(status_code=404, detail=f"Author with id {id} not found.")
    return authors[id]


def save_author(author_in: AuthorBase):
    new_id = max(authors.keys()) +1
    author = AuthorDB(**author_in.model_dump(), id=new_id)
    authors[new_id] = author.model_dump()
    return author


def delete_author(id: int):
    if id not in authors:
        raise HTTPException(status_code=404, detail=f"Author with id {id} not found.")
    del authors[id]
    return {"message": f"Author with id {id} deleted"}


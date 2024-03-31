<<<<<<< HEAD
=======
from typing import Optional

from pydantic import BaseModel
>>>>>>> 108c29042b28a9424dd5b4ee2e02ee40e38ccc47
from sqlmodel import SQLModel, Field

class BookBase(SQLModel):
    id: int
    name: str
    author: str
    year: Optional[int]

class BookDB(BookBase, table=True):
    id: int = Field(default=None, primary_key=True)
    author_id: int = Field(foreign_key="author.id")

class BookCreate(BookBase):
    pass

class AuthorBase(SQLModel):
    name: str

class AuthorDB(AuthorBase, table=True):
    id: int = Field(default=None, primary_key=True)

class AuthorCreate(AuthorBase):
    pass

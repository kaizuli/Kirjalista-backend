from pydantic import BaseModel
from sqlmodel import SQLModel, Field

class BookBase(SQLModel):
    model:str
    author:str

class BookDB(BookBase, table=True):
    id: int = Field(default=None, primary_key=True)

class BookCreate(BookBase):
    pass

class AuthorBase(BaseModel):
    name:str

class AuthorDB(AuthorBase):
    id:int

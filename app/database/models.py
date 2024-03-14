from pydantic import BaseModel
from sqlmodel import SQLModel, Field

class Bookbase(SQLModel):
    model:str
    author:str

class BookDB(Bookbase, table=True):
    id: int = Field(default=None, primary_key=True)

class BookCreate(Bookbase):
    pass

class AuthBase(BaseModel):
    name:str

class AuthDB(AuthBase):
    id:int

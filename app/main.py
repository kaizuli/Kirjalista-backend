import contextlib
from fastapi import FastAPI
from .routers import books, authors
from .database.database import create_db#, add_Books

@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starttaillaan")
    create_db()
#    add_Books()
    yield
    print("Lopetellaan")

app = FastAPI(lifespan=lifespan)

app.include_router(books.router)
app.include_router(authors.router)









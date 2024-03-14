from sqlmodel import SQLModel, Session, create_engine
from models import BookBase, BookDB

books_data = {
    0: {"id": 0, "name": "Sword of Destiny", "author": "Adrzej Sapkowski", "year": 1992},
    1: {"id": 1, "name": "The Last Wish", "author": "Adrzej Sapkowski", "year": 1993},
    2: {"id": 2, "name": "Blood of Elves", "author": "Adrzej Sapkowski", "year": 1994},
    3: {"id": 3, "name": "Time of Contempt", "author": "Adrzej Sapkowski", "year": 1995},
    4: {"id": 4, "name": "Baptism of Fire", "author": "Adrzej Sapkowski", "year": 1996},
    5: {"id": 5, "name": "The Tower of the Swallow", "author": "Adrzej Sapkowski", "year": 1997},
    6: {"id": 6, "name": "The Lady of the Lake", "author": "Adrzej Sapkowski", "year": 1999},
    7: {"id": 7, "name": "Season of Storms", "author": "Adrzej Sapkowski", "year": 2013},
    8: {"id": 8, "name": "Rocannon's World", "author": "Ursula K. Le Guin", "year": 1966},
    9: {"id": 9, "name": "Planet of Exile", "author": "Ursula K. Le Guin", "year": 1967},
    10: {"id": 10, "name": "City of Illusions", "author": "Ursula K. Le Guin", "year": 1967},
    11: {"id": 11, "name": "The Left Hand of Darkness", "author": "Ursula K. Le Guin", "year": 1969},
    12: {"id": 12, "name": "The World for World Is Forest", "author": "Ursula K. Le Guin", "year": 1972},
    13: {"id": 13, "name": "The Dispossessed", "author": "Ursula K. Le Guin", "year": 1974},
    14: {"id": 14, "name": "Four Ways to Forgiveness", "author": "Ursula K. Le Guin", "year": 1995},
    15: {"id": 15, "name": "The Telling", "author": "Ursula K. Le Guin", "year": 2000},
    16: {"id": 16, "name": "Howl's Moving Castle", "author": "Diana Wynne Jones", "year": 1986},
    17: {"id": 15, "name": "Castle in the Air", "author": "Diana Wynne Jones", "year": 1990}
    }

connect_args = {"check_same_thread": False}
engine = create_engine("sqlite:///books.db", echo=True,
                       connect_args=connect_args)

def create_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

#def add_Books(session, books_data):
    # Add books to the database
#    for book_data in books_data:
#        book = BookDB(**book_data)
#        session.add(book)
#    session.commit()


from fastapi import FastAPI

from .db import init_db
from .controllers import auth, books, shelves


app = FastAPI()
app.include_router(auth.router)
app.include_router(books.router)
app.include_router(shelves.router)


@app.on_event("startup")
def on_startup():
    init_db()

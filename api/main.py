from fastapi import FastAPI

from .db import init_db
from .controladores import usuarios


app = FastAPI()
app.include_router(usuarios.router)


@app.on_event("startup")
def on_startup():
    init_db()

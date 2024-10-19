from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime


class BookForm(SQLModel):
    title: str
    summary: str
    author: str
    pages: int
    publication_date: datetime


class Book(BookForm, table=True):
    __tablename__ = "books"

    id: Optional[int] = Field(default=None, primary_key=True)

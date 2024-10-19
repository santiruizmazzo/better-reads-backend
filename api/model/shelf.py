from typing import Optional, List
from sqlmodel import SQLModel, Field


class ShelfForm(SQLModel):
    name: str
    books: List[str]


class Shelf(SQLModel, table=True):
    __tablename__ = "shelves"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

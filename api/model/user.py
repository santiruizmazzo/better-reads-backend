from typing import Optional
from sqlmodel import SQLModel, Field


class UserForm(SQLModel):
    name: str
    last_name: str
    email: str
    password: str


class User(UserForm, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)

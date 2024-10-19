from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..db import get_session
from ..model.book import BookForm

router = APIRouter(tags=["Books"])


@router.get("/books")
def get_books(session: Session = Depends(get_session)):
    # session.add(user)
    # session.commit()
    # session.refresh(user)
    return [
        {
            "title": "It",
            "summary": "Ohhh scary...",
            "author": "Stephen King",
            "pages": 1116,
            "publication_date": "September 15, 1986",
        }
    ]


@router.post("/books")
def create_book(book_form: BookForm, session: Session = Depends(get_session)):
    # session.add(book_form)
    # session.commit()
    # session.refresh(book_form)
    return book_form

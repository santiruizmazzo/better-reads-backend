from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..db import get_session
from ..model.shelf import ShelfForm

router = APIRouter(tags=["Shelves"])


@router.post("/shelves")
def create_shelf(shelf_form: ShelfForm, session: Session = Depends(get_session)):
    # session.add(shelf_form)
    # session.commit()
    # session.refresh(shelf_form)
    return shelf_form

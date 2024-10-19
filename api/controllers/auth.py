from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..db import get_session
from ..model.user import UserForm

router = APIRouter(tags=["Auth"])


@router.post("/login")
def log_user(session: Session = Depends(get_session)):
    # users = session.exec(select(User)).all()
    return "Este endpoint deberia devolver una sesion supongo"


@router.post("/register")
def create_user(user_form: UserForm, session: Session = Depends(get_session)):
    # session.add(user)
    # session.commit()
    # session.refresh(user)
    return user_form

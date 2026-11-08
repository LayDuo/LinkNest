from typing import Annotated

from fastapi import FastAPI, Depends
from sqlmodel import Session, select

from app.database.db import get_session
from app.models.x import X

app = FastAPI()


SessionDep = Annotated[
    Session,
    Depends(get_session)
]


@app.post("/x")
def create_user(x: X, session: SessionDep):
    session.add(x)
    session.commit()
    session.refresh(x)

    return x


@app.get("/x")
def get_users(session: SessionDep):
    statement = select(X)

    x = session.exec(statement).all()

    return x
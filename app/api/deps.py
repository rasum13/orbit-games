from app.models.user import User
from collections.abc import Generator
from typing import Annotated

from fastapi import Depends, Request, HTTPException, status
from sqlmodel import Session

from app.core.db import engine

def get_db() -> Generator[Session]:
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_db)]

def get_current_user(request: Request, session: SessionDep) -> User:
    user_id = request.session.get("user_id")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )

    user = session.get(User, user_id)
    if not user:
        request.session.clear()
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )

    return user


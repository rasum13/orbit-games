from app.core.security import hash_password
from app.models.user import User, UserCreate
from sqlmodel import Session, select

def get_user_by_username(*, session: Session, username: str) -> User | None:
    return session.exec(select(User).where(User.username == username)).first()

def create_user(*, session: Session, user_create: UserCreate) -> User:
    user = User(
        username=user_create.username,
        is_admin=user_create.is_admin,
        hashed_password=hash_password(user_create.password)
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


from sqlalchemy.exc import IntegrityError
from pydantic import ValidationError
from app.services.user import get_user_by_username, create_user
from fastapi.responses import RedirectResponse
from app.core.security import verify_password
from app.models.user import User, UserCreate
from sqlmodel import select
from app.api.deps import SessionDep
from fastapi import APIRouter, Request, Query, Form
from app.core.templates import templates

router = APIRouter()


@router.get(path="/login")
async def login_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={
        }
    )

@router.get(path="/signup")
async def signup_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="signup.html",
        context={
        }
    )

@router.post(path="/login")
async def login(
    session: SessionDep,
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):
    user = get_user_by_username(session=session, username=username)

    if not user or not verify_password(password, user.hashed_password):
        return templates.TemplateResponse(
            request=request,
            name="login.html",
            context={"error": "Invalid username or password"}
        )
    
    request.session["user_id"] = user.id

    return RedirectResponse(url="/store", status_code=303)

@router.post(path="/signup")
async def signup(
    session: SessionDep,
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    password_repeated: str = Form(...)
):
    if password != password_repeated:
        return templates.TemplateResponse(
            request=request,
            name="signup.html",
            context={"error": "passwords do not match"}
        )

    try:
        user_create = UserCreate(username=username, password=password, is_admin=False)
    except ValidationError:
        return templates.TemplateResponse(
            request=request,
            name="signup.html",
            context={"error": "Password must be between 8 and 128 characters"}
        )

    if get_user_by_username(session=session, username=username):
        return templates.TemplateResponse(
            request=request,
            name="signup.html",
            context={"error": "Username already taken"}
        )

    try:
        user = create_user(session=session, user_create=user_create)
    except IntegrityError:
        session.rollback()
        return templates.TemplateResponse(
            request=request,
            name="signup.html",
            context={"error": "Username already taken"}
        )

    request.session["user_id"] = user.id
    
    print("REDIRECTING")
    return RedirectResponse(url="/store", status_code=303)

@router.post(path="/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/login", status_code=303)

@router.get(path="/logout")
async def logout_get(request: Request):
    request.session.clear()
    return RedirectResponse(url="/login", status_code=303)

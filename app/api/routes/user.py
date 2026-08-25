from app.api.deps import SessionDep
from fastapi import APIRouter, Request, Query
from app.core.templates import templates

router = APIRouter()


@router.get(path="/login")
async def login_page(session: SessionDep, request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={
        }
    )

@router.get(path="/signup")
async def signup_page(session: SessionDep, request: Request):
    return templates.TemplateResponse(
        request=request,
        name="signup.html",
        context={
        }
    )

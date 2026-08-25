from fastapi import APIRouter, Request
from app.core.templates import templates

router = APIRouter()

@router.get("/")
async def home_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={}
    )

@router.get("/about")
async def about_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="about.html",
        context={
            "current_page": "about_page"
        }
    )

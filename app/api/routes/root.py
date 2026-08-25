from fastapi import APIRouter, Request
from app.core.templates import templates

router = APIRouter()

@router.get("/about")
async def about_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="about.html",
        context={}
    )

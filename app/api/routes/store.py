from fastapi import APIRouter, Request
from app.core.templates import templates

router = APIRouter()

@router.get("/")
async def store_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="store.html"
    )

@router.get(path="/game")
async def game_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="game.html"
    )

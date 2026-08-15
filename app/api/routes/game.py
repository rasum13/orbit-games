from app.api.deps import SessionDep
from fastapi import APIRouter, Request
from app.core.templates import templates
from app.services.game import get_game

router = APIRouter()

@router.get(path="/{game_id}")
async def game_page(session: SessionDep, request: Request, game_id: int):
    game = get_game(session=session, id=game_id)

    return templates.TemplateResponse(
        request=request,
        name="game.html",
        context={
            "game": game
        }
    )

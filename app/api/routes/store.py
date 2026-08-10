from app.models.game import Game
from app.api.deps import SessionDep
from typing import List
from fastapi import APIRouter, Request, Query
from app.core.templates import templates
from app.services.game import get_games, get_genres, get_game

router = APIRouter()


@router.get("/")
async def store_page(session: SessionDep, request: Request, genres: List[str] = Query([])):
    print(genres)
    games = get_games(session=session)
    genre_list = get_genres(session=session)
    print(genre_list)

    return templates.TemplateResponse(
        request=request,
        name="store.html",
        context={
            "games": games,
            "genre_list": genre_list,
        }
    )

@router.get(path="/game/{game_id}")
async def game_page(session: SessionDep, request: Request, game_id: int):
    game = get_game(session=session, id=game_id)

    return templates.TemplateResponse(
        request=request,
        name="game.html",
        context={
            "game": game
        }
    )

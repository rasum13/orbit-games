from app.api.deps import SessionDep
from typing import List
from fastapi import APIRouter, Request, Query
from app.core.templates import templates
from app.services.game import get_games, get_genres, get_game, get_games_by_genre

router = APIRouter()


@router.get("/")
async def store_page(session: SessionDep, request: Request, filter_genres: List[int] = Query([], alias="filter-genres")):
    games = get_games(session=session)
    genre_list = get_genres(session=session)

    if len(filter_genres) > 0:
        games = get_games_by_genre(session=session, genre_id_list=filter_genres)

    return templates.TemplateResponse(
        request=request,
        name="store.html",
        context={
            "games": games,
            "genre_list": genre_list,
            "filter_genres": filter_genres
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

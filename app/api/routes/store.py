from app.api.deps import SessionDep
from typing import List
from fastapi import APIRouter, Request, Query
from app.core.templates import templates
from app.services.game import get_games, get_genres, get_games_by_genre, search_games

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

@router.get(path="/search")
async def store_search(session: SessionDep, request: Request, query: str = Query()):
    search_results =  search_games(session=session, query=query)
    return templates.TemplateResponse(
        request=request,
        name="search.html",
        context={
            "games": search_results,
        }
    )

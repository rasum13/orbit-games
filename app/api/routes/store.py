from fastapi.responses import RedirectResponse
from app.api.deps import SessionDep, get_current_user
from typing import List
from fastapi import APIRouter, Request, Query, Depends, Form
from app.core.templates import templates
from app.services.game import get_games, get_genres, get_games_by_genre, search_games, add_game_to_cart, get_games_from_cart, remove_game_from_cart, remove_all_games_from_cart

router = APIRouter()


@router.get("/")
async def store_page(session: SessionDep, request: Request, filter_genres: List[int] = Query([], alias="filter-genres"), _ = Depends(get_current_user)):
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
            "filter_genres": filter_genres,
            "current_page": "store_page"
        }
    )

@router.get(path="/search")
async def store_search(session: SessionDep, request: Request, query: str = Query(), _ = Depends(get_current_user)):
    search_results =  search_games(session=session, query=query)
    return templates.TemplateResponse(
        request=request,
        name="search.html",
        context={
            "games": search_results,
            "search_query": query,
            "current_page": "store_page"
        }
    )

@router.get(path="/cart")
async def cart_page(session: SessionDep, request: Request, _ = Depends(get_current_user)):
    games = get_games_from_cart(session=session, request=request)

    total_price = sum(game.price for game in games)

    return templates.TemplateResponse(
        request=request,
        name="cart.html",
        context={
            "games": games,
            "total_price": total_price
        }
    )

@router.get(path="/games_bought")
async def games_bought(request: Request, _ = Depends(get_current_user)):
    return templates.TemplateResponse(
        request=request,
        name="games_bought.html",
        context={}
    )

@router.post(path="/cart/add")
async def cart_add_game(session: SessionDep, request: Request, game_id: int = Form(...), _ = Depends(get_current_user)):
    added = add_game_to_cart(session=session, request=request, game_id=game_id)
    if not added:
        pass
    return RedirectResponse(url="/store/cart", status_code=303)

@router.post(path="/cart/remove")
async def cart_remove_game(session: SessionDep, request: Request, game_id: int = Form(...), _ = Depends(get_current_user)):
    removed = remove_game_from_cart(session=session, request=request, game_id=game_id)
    if not removed:
        pass
    return RedirectResponse(url="/store/cart", status_code=303)

@router.post(path="/cart/buy_all")
async def cart_buy_all(request: Request, _ = Depends(get_current_user)):
    remove_all_games_from_cart(request=request)
    return RedirectResponse(url="/store/games_bought", status_code=303)

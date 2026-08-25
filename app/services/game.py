from typing import List
from fastapi import Request
from sqlalchemy.dialects.postgresql.ext import to_tsvector, websearch_to_tsquery
from app.models.game import Game, GameCreate, Genre
from sqlmodel import Session, select

def get_games(*, session: Session) -> list[Game]:
    statement = select(Game)
    games = session.exec(statement)

    return list(games)

def get_games_by_genre(*, session: Session, genre_id_list: list[int]) -> list[Game]:
    statement_games = select(Game)
    games = session.exec(statement_games).all()

    target_genre_ids= set(genre_id_list)
    games_filtered = [game for game in games if target_genre_ids.issubset({g.id for g in game.genres})]

    return list(games_filtered)

def search_games(*, session: Session, query: str) -> list[Game]:
    statement = select(Game).where(to_tsvector("english", Game.title).bool_op("@@")(websearch_to_tsquery("english", query)))
    search_results = session.exec(statement)
    return list(search_results)

def get_game(*, session: Session, id: int) -> Game | None:
    game = session.get(Game, id)

    return game

def get_genres(*, session: Session) -> list[Genre]:
    statement = select(Genre)
    genres = session.exec(statement)

    return list(genres)

def create_game(*, session: Session, game_in: GameCreate) -> Game:
    genres: list[Genre] = []
    for genre_name in game_in.genre_names:
        statement = select(Genre).where(Genre.name == genre_name)
        existing_genre = session.exec(statement).first()

        if existing_genre:
            genres.append(existing_genre)
        else:
            new_genre = Genre(name=genre_name)
            session.add(new_genre)
            genres.append(new_genre)

    db_game = Game.model_validate(game_in, update={"genres": genres})

    session.add(db_game)
    session.commit()
    session.refresh(db_game)

    return db_game

def add_game_to_cart(*, session: Session, request: Request, game_id: int) -> bool:
    cart: List[int] = request.session.get("cart", [])
    game = get_game(session=session, id=game_id)
    if game and game.id not in cart:
        cart.append(game.id) # type: ignore
        request.session["cart"] = cart
        return True
    return False

def remove_game_from_cart(*, session: Session, request: Request, game_id: int) -> bool:
    cart: List[int] = request.session.get("cart", [])

    if game_id in cart:
        cart.remove(game_id)
        request.session["cart"] = cart
        return True
    return False

def get_games_from_cart(*, session: Session, request: Request) -> List[Game]:
    cart = request.session.get("cart", [])

    if not cart:
        return []

    statement = select(Game).where(Game.id.in_(cart)) # type: ignore
    games = session.exec(statement).all()

    return list(games)

def remove_all_games_from_cart(*, request: Request):
    request.session["cart"] = []

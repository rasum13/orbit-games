from app.models.game import Game, GameCreate, Genre
from sqlmodel import Session, select

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


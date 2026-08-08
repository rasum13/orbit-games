from decimal import Decimal
from sqlmodel import Field, SQLModel, Relationship

class Game(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    description: str
    price: Decimal = Field(default=0, max_digits=5, decimal_places=2)
    genres: list["Genre"] = Relationship(back_populates="games")

    card_image: str
    banner_image: str

class Genre(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    games: list["Game"] = Relationship(back_populates="genres")

class GameGenreLink(SQLModel, table=True):
    game_id: int | None = Field(default=None, foreign_key="game.id", primary_key=True)
    genre_id: int | None = Field(default=None, foreign_key="genre.id", primary_key=True)

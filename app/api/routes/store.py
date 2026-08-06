from ntpath import join
from fastapi import APIRouter, Request
from app.core.templates import templates

router = APIRouter()

games = [
    {
        "id": "hollow-knight",
        "title": "Hollow Knight",
        "description": "Forge your own path in Hollow Knight! An epic action adventure through a vast ruined kingdom of insects and heroes. Explore twisting caverns, battle tainted creatures and befriend bizarre bugs, all in a classic, hand-drawn 2D style.",
        "price": "$6.99",
        "genres": ["Metroidvania", "Action", "Adventure", "Exploration"],
        "card_image": "hollow-knight.png",
        "banner_image": "hollow-knight-banner.png"
    },
    {
        "id": "rdr2",
        "title": "Red Dead Redemption II",
        "description": " Arthur Morgan and the Van der Linde Gang are outlaws on the run. With federal agents and bounty hunters massing on their heels, the gang must rob, steal, and fight their way across the rugged heartland in order to survive.",
        "price": "$59.99",
        "genres": ["Open World", "Western", "Multiplayer"],
        "card_image": "rdr2.png",
        "banner_image": "rdr2-banner.png"
    },
    {
        "id": "bmw",
        "title": "Black Myth: Wukong",
        "description": "Black Myth: Wukong is an action RPG rooted in Chinese mythology. You shall set out as the Destined One to venture into the challenges and marvels ahead, to uncover the obscured truth beneath the veil of a glorious legend from the past.",
        "price": "$59.99",
        "genres": ["Mythology", "Action", "RPG", "Souls-like"],
        "card_image": "bmw.png",
        "banner_image": "bmw-banner.png"
    },
    {
        "id": "dark-souls",
        "title": "Dark Souls: Remastered",
        "description": "Then, there was fire. Re-experience the critically acclaimed, genre-defining game that started it all. Beautifully remastered, return to Lordran in stunning high-definition detail running at 60fps.",
        "price": "$39.99",
        "genres": ["Souls-like", "Dark Fantasy", "RPG", "Action"],
        "card_image": "dark-souls.png",
        "banner_image": "dark-souls-banner.png"
    },
    {
        "id": "hk-silksong",
        "title": "Hollow Knight: Silksong",
        "description": "Discover a vast, haunted kingdom in Hollow Knight: Silksong! Explore, fight and survive as you ascend to the peak of a land ruled by silk and song.",
        "price": "$8.19",
        "genres": ["Metroidvania", "Action", "Souls-like", "Exploration"],
        "card_image": "hk-silksong.png",
        "banner_image": "hk-silksong-banner.png"
    },
    {
        "id": "outer-wilds",
        "title": "Outer Wilds",
        "description": "Named Game of the Year 2019 by Giant Bomb, Polygon, Eurogamer, and The Guardian, Outer Wilds is a critically-acclaimed and award-winning open world mystery about a solar system trapped in an endless time loop.",
        "price": "$11.99",
        "genres": ["Space", "Exploration", "Mystery", "Adventure"],
        "card_image": "outer-wilds.png",
        "banner_image": "outer-wilds-banner.png"
    },
]

@router.get("/")
async def store_page(request: Request):
    genre_list= []

    for game in games:
        for genre in game["genres"]:
            new_genre = {"name": genre, "id": "-".join(genre.lower().split(" "))}
            if new_genre not in genre_list:
                genre_list.append(new_genre)

    return templates.TemplateResponse(
        request=request,
        name="store.html",
        context={
            "games": games,
            "genre_list": genre_list,
        }
    )

@router.get(path="/game/{game_id}")
async def game_page(request: Request, game_id: str):
    game_details: dict[str, str | list[str]]
    for game in games:
        if game["id"] == game_id:
            game_details = game
            break

    return templates.TemplateResponse(
        request=request,
        name="game.html",
        context={
            "game": game_details
        }
    )

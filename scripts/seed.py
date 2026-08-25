from app.services.game import create_game
from app.models.game import Game, GameCreate
from app.core.db import engine
from sqlmodel import Session

games = [
    {
        "id": "hollow-knight",
        "title": "Hollow Knight",
        "description": "Forge your own path in Hollow Knight! An epic action adventure through a vast ruined kingdom of insects and heroes. Explore twisting caverns, battle tainted creatures and befriend bizarre bugs, all in a classic, hand-drawn 2D style.",
        "price": 6.99,
        "genres": ["Metroidvania", "Action", "Adventure", "Exploration","Souls-like"],
        "card_image": "hollow-knight.png",
        "banner_image": "hollow-knight-banner.png"
    },
    {
        "id": "rdr2",
        "title": "Red Dead Redemption II",
        "description": " Arthur Morgan and the Van der Linde Gang are outlaws on the run. With federal agents and bounty hunters massing on their heels, the gang must rob, steal, and fight their way across the rugged heartland in order to survive.",
        "price": 59.99,
        "genres": ["Open World","Western","Story Rich","Singleplayer","Action"],
        "card_image": "rdr2.png",
        "banner_image": "rdr2-banner.png"
    },
    {
        "id": "bmw",
        "title": "Black Myth: Wukong",
        "description": "Black Myth: Wukong is an action RPG rooted in Chinese mythology. You shall set out as the Destined One to venture into the challenges and marvels ahead, to uncover the obscured truth beneath the veil of a glorious legend from the past.",
        "price": 59.99,
        "genres": ["Mythology", "Action", "RPG", "Souls-like"],
        "card_image": "bmw.png",
        "banner_image": "bmw-banner.png"
    },
    {
        "id": "dark-souls",
        "title": "Dark Souls: Remastered",
        "description": "Then, there was fire. Re-experience the critically acclaimed, genre-defining game that started it all. Beautifully remastered, return to Lordran in stunning high-definition detail running at 60fps.",
        "price": 39.99,
        "genres": ["Souls-like", "Dark Fantasy", "RPG", "Action"],
        "card_image": "dark-souls.png",
        "banner_image": "dark-souls-banner.png"
    },
    {
        "id": "hk-silksong",
        "title": "Hollow Knight: Silksong",
        "description": "Discover a vast, haunted kingdom in Hollow Knight: Silksong! Explore, fight and survive as you ascend to the peak of a land ruled by silk and song.",
        "price": 8.19,
        "genres": ["Metroidvania", "Action", "Souls-like", "Exploration"],
        "card_image": "hk-silksong.png",
        "banner_image": "hk-silksong-banner.png"
    },
    {
        "id": "outer-wilds",
        "title": "Outer Wilds",
        "description": "Named Game of the Year 2019 by Giant Bomb, Polygon, Eurogamer, and The Guardian, Outer Wilds is a critically-acclaimed and award-winning open world mystery about a solar system trapped in an endless time loop.",
        "price": 11.99,
        "genres": ["Space", "Exploration", "Mystery", "Adventure"],
        "card_image": "outer-wilds.png",
        "banner_image": "outer-wilds-banner.png"
    },
    {
        "id": "cod-ii",
        "title": "Call of Duty: Black Ops II",
        "description": "Pushing the boundaries of what fans have come to expect from the record-setting entertainment franchise, Call of Duty: Black Ops II propels players into a near future Cold War.",
        "price": 39.99,
        "genres": ["Multiplayer","Action","FPS","Shooter","SinglePlayer","Co-op"],
        "card_image": "cod-ii.png",
        "banner_image": "cod-ii-background.png"
    },
    {
        "id": "elden-ring",
        "title": "ELDEN RING",
        "description": "THE CRITICALLY ACCLAIMED FANTASY ACTION RPG. Rise, Tarnished, and be guided by grace to brandish the power of the Elden Ring and become an Elden Lord in the Lands Between.",
        "price": 59.99,
        "genres": ["Souls-like","Open World","Dark Fantasty","RPG"],
        "card_image": "elden-ring.png",
        "banner_image": "elden-ring-background.png"
    },
    {
        "id": "froza-horizon",
        "title": "Froza Horizon 6",
        "description": "Discover the breathtaking landscapes of Japan in over 550 real-world cars and become a racing Legend in Forza Horizon's biggest open world driving adventure yet.",
        "price": 48.99,
        "genres": ["Racing","Open World","Driving","Multiplayer"],
        "card_image": "froza-horizon.png",
        "banner_image": "froza-horizon-background.png"
    },
    {
        "id": "hades",
        "title": "Hades",
        "description": "Defy the god of the dead as you hack and slash out of the Underworld in this rogue-like dungeon crawler from the creators of Bastion, Transistor, and Pyre.",
        "price": 8.49,
        "genres": ["Action","Roguelike","Roguelite","Hack and Slash","RPG","Indie"],
        "card_image": "hades.png",
        "banner_image": "hades-background.png"
    },
    {
        "id": "last-of-us",
        "title": "The Last of Us Part I",
        "description": "Discover the award-winning game that inspired the critically acclaimed television show. Guide Joel and Ellie through a post-apocalyptic America, and encounter unforgettable allies and enemies in The Last of Us.",
        "price": 59.99,
        "genres": ["Story Rich","Zombie","Horror","Shooter","Post-apocalyptic"],
        "card_image": "last-of-us.png",
        "banner_image": "last-of-us-background.png"
    },
    {
        "id": "witcher-III",
        "title": "The Witcher 3: Wild Hunt",
        "description": "You are Geralt of Rivia, mercenary monster slayer. Before you stands a war-torn, monster-infested continent you can explore at will. Your current contract? Tracking down Ciri — the Child of Prophecy, a living weapon that can alter the shape of the world.",
        "price": 39.99,
        "genres": ["Open World","RPG","Story Rich","Fantasy","Atmospheric"],
        "card_image": "witcher-III.png",
        "banner_image": "witcher-III-background.png"
    },
    {
        "id": "rdr",
        "title": "Red Dead Redemption",
        "description": "Experience the story of former outlaw John Marston as he tracks down the last remaining members of the notorious Van der Linde Gang in the PC debut of the critically acclaimed predecessor to Red Dead Redemption 2.",
        "price": 49.99,
        "genres": ["Open World","Western","Story Rich","Singleplayer","Action"],
        "card_image": "rdr.png",
        "banner_image": "rdr-background.png"
    },
    {
        "id": "hades-II",
        "title": "Hades II",
        "description": "Battle beyond the Underworld using dark sorcery to take on the Titan of Time in this bewitching sequel to the award-winning rogue-like dungeon crawler.",
        "price": 10.49,
        "genres": ["Action","Roguelike","Roguelite","Hack and Slash","RPG","Indie"],
        "card_image": "hades-II.png",
        "banner_image": "hades-II-background.png"
    },
    {
        "id": "resident-evil",
        "title": "Resident Evil 4",
        "description": "Survival is just the beginning. Six years have passed since the biological disaster in Raccoon City. Leon S. Kennedy, one of the survivors, tracks the president's kidnapped daughter to a secluded European village, where there is something terribly wrong with the locals.",
        "price": 32.99,
        "genres": ["Action","Horror","Third-Person Shooter","Survival Horror"],
        "card_image": "resident-evil.png",
        "banner_image": "resident-evil-background.png"
    },
    {
        "id": "cod-iii",
        "title": "Call of Duty: Black Ops III",
        "description": "Call of Duty: Black Ops III Zombies Chronicles Edition includes the full base game plus the Zombies Chronicles content expansion.",
        "price": 59.99,
        "genres": ["Multiplayer","Action","FPS","Shooter","SinglePlayer","Co-op"],
        "card_image": "cod-iii.png",
        "banner_image": "cod-iii-background.png"
    },
    {
        "id": "darksouls-iii",
        "title": "DARK SOULS III",
        "description": "Dark Souls continues to push the boundaries with the latest, ambitious chapter in the critically-acclaimed and genre-defining series. Prepare yourself and Embrace The Darkness!",
        "price": 59.99,
        "genres": ["Souls-like", "Dark Fantasy", "RPG", "Action"],
        "card_image": "darksouls-III.png",
        "banner_image": "darksouls-III-background.png"
    },
]

def seed_db():
    with Session(engine) as session:
        for game in games:
            new_game = GameCreate.model_validate(game, update={"genre_names": game["genres"]})
            create_game(session=session, game_in=new_game)


if __name__ == "__main__":
    seed_db()

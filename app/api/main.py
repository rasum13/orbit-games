from fastapi import APIRouter
from app.api.routes import store, game, user, root

api_router = APIRouter()
api_router.include_router(root.router, prefix="", tags=["root"])
api_router.include_router(store.router, prefix="/store", tags=["store"])
api_router.include_router(game.router, prefix="/game", tags=["game"])
api_router.include_router(user.router, prefix="/user", tags=["user"])

from fastapi import APIRouter
from app.api.routes import store, game, user

api_router = APIRouter()
api_router.include_router(store.router, prefix="", tags=["store"])
api_router.include_router(game.router, prefix="/game", tags=["game"])
api_router.include_router(user.router, prefix="/user", tags=["user"])

from starlette.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.api.main import api_router
from app.core.config import settings

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(_: Request, exc: StarletteHTTPException):
    if exc.status_code == 401:
        return RedirectResponse(url="/user/login", status_code=303)
    elif exc.status_code == 404:
        return RedirectResponse(url="/404", status_code=303)
    raise exc

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)

app.include_router(api_router)

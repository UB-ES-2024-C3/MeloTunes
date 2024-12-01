""" Main API routes definition """
from fastapi import APIRouter

from app.api.routes import login, users, utils, songs, albums

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(songs.router, prefix="/songs", tags=["songs"])
api_router.include_router(albums.router, prefix="/albums", tags=["albums"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])

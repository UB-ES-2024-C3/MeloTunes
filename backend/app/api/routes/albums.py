""" User management routes """
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.sql.functions import current_user
from sqlmodel import col, delete, func, select

from app import crud
from app.api.deps import (
    CurrentUser,
    SessionDep,
    get_current_active_superuser,
)
from app.core.config import settings
from app.models import (
    Message,
    Album,
    AlbumCreate,
    AlbumCreateOpen,
    AlbumOut,
    AlbumsOut,
    AlbumUpdate
)

router = APIRouter()


@router.get(
    "/",
    # dependencies=[Depends(get_current_active_superuser)],
    response_model=AlbumsOut
)
def read_albums(session: SessionDep, skip: int = 0, limit: int = 100) -> Any:
    """
    Retrieve albums.
    """

    count_statement = select(func.count()).select_from(Album)
    count = session.exec(count_statement).one()

    statement = select(Album).offset(skip).limit(limit)
    albums = session.exec(statement).all()

    return AlbumsOut(data=albums, count=count)


@router.post(
    "/",
    response_model=AlbumOut
)
def create_album(*, session: SessionDep, album_in: AlbumCreate) -> Any:
    """
    Create new album.
    """
    album = crud.album.get_album_by_title_and_artist(session=session, title=album_in.title, artist=CurrentUser.artist_name)
    if album:
        raise HTTPException(
            status_code=400,
            detail="The album already exists in the system.",
        )
    #album_in.artist = CurrentUser.artist_name
    album = crud.album.create_album(session=session, album_create=album_in)
    return album


"""
@router.patch("/me", response_model=SongOut)
def update_song_me(*, session: SessionDep, song_in: SongUpdateMe, current_user: CurrentUser) -> Any:

    Update own user.

    if song_in.title and song_in.artist:
        existing_song = crud.user.get_song_by_title_and_artist(session=session, title=song_in.title, artist=song_in.artist)
        if existing_song and existing_song.artist != current_user.first_name.concat("" + current_user.second_name):
            raise HTTPException(
                status_code=409, detail="Song with this title already exists"
            )
    song_data = song_in.model_dump(exclude_unset=True)
    current_user.sqlmodel_update(song_data)
    session.add(current_user)
    session.commit()
    session.refresh(current_user)
    return current_user
"""

"""
@router.get("/me", response_model=UserOut)
def read_user_me(session: SessionDep, current_user: CurrentUser) -> Any:

    Get current user.

    return current_user


@router.post("/open", response_model=UserOut)
def create_user_open(session: SessionDep, user_in: UserCreateOpen) -> Any:

    Create new user without the need to be logged in.

    if not settings.USERS_OPEN_REGISTRATION:
        raise HTTPException(
            status_code=403,
            detail="Open user registration is forbidden on this server",
        )
    user = crud.user.get_user_by_email(session=session, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system",
        )
    user_create = UserCreate.from_orm(user_in)
    user = crud.user.create_user(session=session, user_create=user_create)
    return user
"""


@router.get("/{album_id}", response_model=AlbumOut)
def read_album_by_id(album_id: int, session: SessionDep) -> Any:
    """
    Get a specific album by id.
    """
    album = session.get(Album, album_id)
    return album


@router.get("/albums/{album_title}", response_model=AlbumsOut)
def read_album_by_title(album_title: str, session: SessionDep) -> Any:
    """
    Get a specific album by title.
    """
    albums = crud.album.get_album_by_title(session=session, title=album_title)
    return AlbumsOut(data=albums, count=len(albums))


@router.patch(
    "/{album_id}",
    response_model=AlbumOut,
)
def update_album(*, session: SessionDep, album_id: int, album_in: AlbumUpdate) -> Any:
    """
    Update an album.
    """
    db_album = session.get(Album, album_id)
    if not db_album:
        raise HTTPException(
            status_code=404,
            detail="The album with this id does not exist in the system",
        )
    if CurrentUser.artist_name != db_album.artist and CurrentUser.is_superuser == False:
        raise HTTPException(
            status_code=409, detail="This album does not belong to you"
        )

    db_album = crud.album.update_album(session=session, db_album=db_album, album_in=album_in)
    return db_album


@router.delete("/{album_id}")
def delete_album(session: SessionDep, album_id: int) -> Message:
    """
    Delete an album.
    """
    album = session.get(Album, album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    #elif album.artist != current_user.artist_name and not current_user.is_superuser:
     #   raise HTTPException(
      #      status_code=403, detail="The user doesn't have enough privileges"
       # )

    session.delete(album)
    session.commit()
    return Message(message="Album deleted successfully")

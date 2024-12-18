""" User management routes """
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
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
    Song,
    SongCreate,
    SongCreateOpen,
    SongOut,
    SongsOut,
    SongUpdate,
    Album,
    User
)

router = APIRouter()


@router.get(
    "/",
    #dependencies=[Depends(get_current_active_superuser)],
    response_model=SongsOut
)
def read_songs(session: SessionDep, skip: int = 0, limit: int = 100) -> Any:
    """
    Retrieve songs.
    """

    count_statement = select(func.count()).select_from(Song)
    count = session.exec(count_statement).one()

    statement = select(Song).offset(skip).limit(limit)
    songs = session.exec(statement).all()

    return SongsOut(data=songs, count=count)


@router.post(
    "/",
    response_model=SongOut
)
def create_song(*, session: SessionDep, song_in: SongCreate) -> Any:
    """
    Create new song.
    """
    song = crud.song.get_song_by_title_and_artist(session=session, title=song_in.title, artist=song_in.artist)
    if song:
        raise HTTPException(
            status_code=400,
            detail="The song already exists in the system.",
        )

    song = crud.song.create_song(session=session, song_create=song_in)
    return song

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

@router.get("/{song_id}", response_model=SongOut)
def read_song_by_id(song_id: int, session: SessionDep) -> Any:
    """
    Get a specific song by id.
    """
    song = session.get(Song, song_id)
    return song

@router.get("/songs/{song_title}", response_model=SongsOut)
def read_song_by_title(song_title: str, session: SessionDep) -> Any:
    """
    Get a specific song by title.
    """
    songs = crud.song.get_song_by_title(session=session, title=song_title)
    return SongsOut(data=songs, count=len(songs))


@router.get("/songs/artist/{songs_artist}", response_model=SongsOut)
def read_songs_by_artist(songs_artist: str, session: SessionDep, skip: int = 0, limit: int = 100) -> Any:
    """
    Get a specific song by artist.
    """
    print("Iniciando consulta...")
    
    # Define el statement antes de usarlo
    statement = select(Song).offset(skip).limit(limit).where(func.lower(Song.artist).contains(songs_artist.lower()))
    print(f"Consulta generada: {statement}")

    # Ejecuta el statement después de definirlo
    songs = session.exec(statement).all()
    print(f"Resultados obtenidos: {songs}")

    count_statement = select(func.count()).select_from(Song)
    count = session.exec(count_statement).one()
    
    return SongsOut(data=songs, count=count)


@router.patch(
    "/{song_id}",
    response_model=SongOut,
)
def update_song(*, session: SessionDep, song_id: int, song_in: SongUpdate) -> Any:
    """
    Update a song.
    """
    db_song = session.get(Song, song_id)
    if not db_song:
        raise HTTPException(
            status_code=404,
            detail="The song with this id does not exist in the system",
        )
    if CurrentUser.first_name.concat("" + CurrentUser.second_name) != db_song.artist and CurrentUser.is_superuser == False:
        raise HTTPException(
            status_code=409, detail="This song does not belong to you"
        )

    db_song = crud.song.update_song(session=session, db_song=db_song, song_in=song_in)
    return db_song


@router.delete("/{song_id}/{user_id}")
def delete_song(session: SessionDep, song_id: int, user_id: int) -> Message:
    """
    Delete a song.
    """
    user = session.get(User, user_id)
    song = session.get(Song, song_id)
    if not song:
        raise HTTPException(status_code=404, detail="Song not found")
    elif song.artist != user.artist_name and not user.is_superuser:
        raise HTTPException(
            status_code=403, detail="The user doesn't have enough privileges"
        )

    session.delete(song)
    session.commit()
    return Message(message="Song deleted successfully")


@router.patch(
    "/song2album/",
    response_model=SongOut,
)
def add_song_to_album(*, session: SessionDep, current_user: CurrentUser, song_id: int, album_id: int, song_in: SongUpdate) -> Any:
    """
    Update a song.
    """
    db_song = session.get(Song, song_id)
    db_album = session.get(Album, album_id)
    if not db_song:
        raise HTTPException(
            status_code=404,
            detail="The song with this id does not exist in the system",
        )
    if not db_album:
        raise HTTPException(
            status_code=404,
            detail="The album with this id does not exist in the system",
        )
    if current_user.artist_name != db_song.artist:
        raise HTTPException(
            status_code=409, detail=db_song.artist
        )
    if current_user.artist_name != db_album.artist and current_user.is_superuser == False:
        raise HTTPException(
            status_code=409, detail="This album does not belong to you"
        )
    db_song.album = db_album.title
    db_song = crud.song.update_song(session=session, db_song=db_song, song_in=song_in)
    return db_song

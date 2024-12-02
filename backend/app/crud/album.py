""" User related CRUD methods """
from typing import Any

from sqlmodel import Session, select

from app.models import Album, AlbumCreate, AlbumUpdate



def create_album(*, session: Session, album_create: AlbumCreate) -> Album:
    db_obj = Album.model_validate(
        album_create
    )
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj


def update_album(*, session: Session, db_album: Album, album_in: AlbumUpdate) -> Any:
    album_data = album_in.model_dump(exclude_unset=True)
    extra_data = {}
    db_album.sqlmodel_update(album_data, update=extra_data)
    session.add(db_album)
    session.commit()
    session.refresh(db_album)
    return db_album


def get_album_by_title_and_artist(*, session: Session, title: str, artist: str) -> Album | None:
    statement = select(Album).where(Album.title == title and  Album.artist == artist)
    session_album = session.exec(statement).first()
    return session_album

def get_album_by_title(*, session: Session, title: str) -> list[Album] | None:
    statement = select(Album).where(Album.title.contains(title.lower()))
    session_album = session.exec(statement).all()
    return session_album

def get_album_by_artist(*, session: Session, artist: str) -> Album | None:
    statement = select(Album).where(Album.artist.contains(artist.lower()))
    session_album = session.exec(statement)
    return session_album
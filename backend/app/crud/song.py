""" User related CRUD methods """
from typing import Any

from sqlmodel import Session, select

from app.models import Song, SongCreate, SongUpdate



def create_song(*, session: Session, song_create: SongCreate) -> Song:
    db_obj = Song.model_validate(
        song_create
    )
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj


def update_song(*, session: Session, db_song: Song, song_in: SongUpdate) -> Any:
    song_data = song_in.model_dump(exclude_unset=True)
    extra_data = {}
    db_song.sqlmodel_update(song_data, update=extra_data)
    session.add(db_song)
    session.commit()
    session.refresh(db_song)
    return db_song


def get_song_by_title_and_artist(*, session: Session, title: str, artist: str) -> Song | None:
    statement = select(Song).where(Song.title == title and  Song.artist == artist)
    session_song = session.exec(statement).first()
    return session_song

def get_song_by_title(*, session: Session, title: str) -> list[Song] | None:
    statement = select(Song).where(Song.title.contains(title.lower()))
    session_song = session.exec(statement).all()
    return session_song

def get_song_by_artist(*, session: Session, artist: str) -> list[Song] | None:
    statement = select(Song).where(Song.artist.contains(artist.lower()))
    session_song = session.exec(statement).all()
    return session_song
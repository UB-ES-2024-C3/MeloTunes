""" User models """
from datetime import timedelta
from datetime import datetime
from typing import List

from sqlmodel import Field, Relationship

from . import userSongLink
from .base import SQLModel

# Shared properties
class AlbumBase(SQLModel):
    title: str
    artist: str
    duration: timedelta
    number_of_songs: int | None = None
    timestamp: datetime


# Database model, database table inferred from class name
class Album(AlbumBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

# Properties to receive via API on creation
class AlbumCreate(AlbumBase):
    pass


class AlbumCreateOpen(SQLModel):
    title: str
    artist: str


# Properties to receive via API on update, all are optional
class AlbumUpdate(AlbumBase):
    artist: str | None = None
    title: str | None = None


# Properties to return via API, id is always required
class AlbumOut(AlbumBase):
    id: int

class AlbumsOut(SQLModel):
    data: list[AlbumOut]
    count: int

# Generic message
class Message(SQLModel):
    message: str

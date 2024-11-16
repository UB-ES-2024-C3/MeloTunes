""" User models """
from datetime import timedelta
from datetime import datetime

from sqlmodel import Field
from .base import SQLModel

# Shared properties
class SongBase(SQLModel):
    title: str
    artist: str
    duration: timedelta
    album: str | None = None
    timestamp: datetime


# Database model, database table inferred from class name
class Song(SongBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

# Properties to receive via API on creation
class SongCreate(SongBase):
    pass


class SongCreateOpen(SQLModel):
    title: str
    artist: str
    album: str | None = None


# Properties to receive via API on update, all are optional
class SongUpdate(SongBase):
    artist: str | None = None


class SongUpdateMe(SQLModel):
    title: str | None = None
    album: str | None = None


# Properties to return via API, id is always required
class SongOut(SongBase):
    id: int

class SongsOut(SQLModel):
    data: list[SongOut]
    count: int

# Generic message
class Message(SQLModel):
    message: str

from sqlmodel import Field
from .base import SQLModel

class userSongLink(SQLModel, table=True):
    user_id: int = Field(default=None, foreign_key="user.id", primary_key=True)
    song_id: int = Field(default=None, foreign_key="song.id", primary_key=True)
""" User models """
from datetime import timedelta
from datetime import datetime

from sqlmodel import Field, Relationship

from .base import SQLModel

# Shared properties
class CommentBase(SQLModel):
    text: str
    user: str
    song: str | None = None
    timestamp: datetime


# Database model, database table inferred from class name
class Comment(CommentBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

# Properties to receive via API on creation
class CommentCreate(CommentBase):
    pass


class CommentCreateOpen(SQLModel):
    text: str


# Properties to receive via API on update, all are optional
class CommentUpdate(CommentBase):
    text: str | None = None


# Properties to return via API, id is always required
class CommentOut(CommentBase):
    id: int

class CommentsOut(SQLModel):
    data: list[CommentOut]
    count: int

# Generic message
class Message(SQLModel):
    message: str

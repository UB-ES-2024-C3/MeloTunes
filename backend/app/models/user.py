""" User models """
from sqlmodel import Field, Relationship
from .base import SQLModel
from .userSong import userSongLink


# Shared properties
class UserBase(SQLModel):
    email: str = Field(unique=True, index=True)
    is_active: bool = True
    is_superuser: bool = False
    first_name: str | None = None
    second_name: str | None = None
    description: str | None = None
    is_artist: bool = False

# Database model, database table inferred from class name
class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: str
    favourite_songs: list["Song"] = Relationship(back_populates="users_liked_me", link_model=userSongLink)

# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str


# TODO replace email str with EmailStr when sqlmodel supports it
class UserCreateOpen(SQLModel):
    email: str
    password: str
    first_name: str
    second_name: str | None = None
    description: str | None = None


# Properties to receive via API on update, all are optional
class UserUpdate(UserBase):
    email: str | None = None  # type: ignore
    password: str | None = None
    is_artist: bool | None = None


# TODO replace email str with EmailStr when sqlmodel supports it
class UserUpdateMe(SQLModel):
    first_name: str | None = None
    second_name: str | None = None
    email: str | None = None
    description: str | None = None

class UpdatePassword(SQLModel):
    current_password: str
    new_password: str

# Properties to return via API, id is always required
class UserOut(UserBase):
    id: int

class UsersOut(SQLModel):
    data: list[UserOut]
    count: int

# Generic message
class Message(SQLModel):
    message: str


# JSON payload containing access token
class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"


# Contents of JWT token
class TokenPayload(SQLModel):
    sub: int | None = None


class NewPassword(SQLModel):
    token: str
    new_password: str

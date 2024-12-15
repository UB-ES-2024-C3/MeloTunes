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
    Comment,
    CommentCreate,
    CommentCreateOpen,
    CommentOut,
    CommentsOut,
    CommentUpdate
)

router = APIRouter()


@router.get(
    "/",
    # dependencies=[Depends(get_current_active_superuser)],
    response_model=CommentsOut
)
def read_comments(session: SessionDep, skip: int = 0, limit: int = 100) -> Any:
    """
    Retrieve comments.
    """

    count_statement = select(func.count()).select_from(Comment)
    count = session.exec(count_statement).one()

    statement = select(Comment).offset(skip).limit(limit)
    comments = session.exec(statement).all()

    return CommentsOut(data=comments, count=count)


@router.post(
    "/",
    response_model=CommentOut
)
def create_comment(*, session: SessionDep, comment_in: CommentCreate) -> Any:
    """
    Create new comment.
    """
    comment = crud.comment.create_comment(session=session, comment_create=comment_in)
    return comment


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


@router.get("/{comment_id}", response_model=CommentOut)
def read_comment_by_id(comment_id: int, session: SessionDep) -> Any:
    """
    Get a specific comment by id.
    """
    comment = session.get(Comment, comment_id)
    return comment


@router.get("/comments/{song_title}", response_model=CommentsOut)
def read_comments_by_song(song_title: str, session: SessionDep) -> Any:
    """
    Get a specific comment by title.
    """
    comments = crud.comment.get_comments_by_song(session=session, song=song_title)
    return CommentsOut(data=comments, count=len(comments))

@router.get("/comments/{user_name}", response_model=CommentsOut)
def read_comments_by_user(user: str, session: SessionDep) -> Any:
    """
    Get a specific comment by title.
    """
    comments = crud.comment.get_comments_by_user(session=session, user=user)
    return CommentsOut(data=comments, count=len(comments))



@router.delete("/{comment_id}")
def delete_comment(session: SessionDep, current_user: CurrentUser, comment_id: int) -> Message:
    """
    Delete a comment.
    """
    comment = session.get(Comment, comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    elif comment.user != current_user.artist_name and not current_user.is_superuser:
        raise HTTPException(
            status_code=403, detail="The user doesn't have enough privileges"
        )

    session.delete(comment)
    session.commit()
    return Message(message="Comment deleted successfully")

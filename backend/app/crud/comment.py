""" User related CRUD methods """
from typing import Any

from sqlmodel import Session, select

from app.models import Comment, CommentCreate, CommentUpdate



def create_comment(*, session: Session, comment_create: CommentCreate) -> Comment:
    db_obj = Comment.model_validate(
        comment_create
    )
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj


#def update_album(*, session: Session, db_album: Album, album_in: AlbumUpdate) -> Any:
 #   album_data = album_in.model_dump(exclude_unset=True)
  #  extra_data = {}
   # db_album.sqlmodel_update(album_data, update=extra_data)
    #session.add(db_album)
    #session.commit()
    #session.refresh(db_album)
    #return db_album


def get_comment_by_song_and_user(*, session: Session, song: str, user: str) -> Comment | None:
    statement = select(Comment).where(Comment.song == song and  Comment.user == user)
    session_album = session.exec(statement).first()
    return session_album

def get_comments_by_song(*, session: Session, song: str) -> list[Comment] | None:
    statement = select(Comment).where(Comment.song == song)
    session_album = session.exec(statement).all()
    return session_album

def get_comments_by_user(*, session: Session, user: str) -> list[Comment] | None:
    statement = select(Comment).where(Comment.user ==user)
    session_album = session.exec(statement).all()
    return session_album
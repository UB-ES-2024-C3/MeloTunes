from fastapi.testclient import TestClient
from sqlmodel import Session
from app.main import app
from app.core.config import settings
from app.models import CommentCreate, UserCreateOpen, Comment, UserTest
from app import crud
from app.tests.utils.utils import random_lower_string, random_email
from datetime import datetime

client = TestClient(app)
comment_id = 0

def test_read_comments() -> None:
    """
    Test to retrieve all comments.
    """
    response = client.get(f"{settings.API_V1_STR}/comments/")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert "count" in data

def test_create_comment() -> None:
    """
    Test to create a new comment.
    """
    comment_data = {
        "text": "Comentario de prueba",
        "user": 'user',
        "song_id": 1,
        "timestamp": datetime.utcnow().isoformat()
    }
    response = client.post(f"{settings.API_V1_STR}/comments/", json=comment_data)
    assert response.status_code == 200
    data = response.json()
    global comment_id
    comment_id = data["id"]
    assert data["text"] == comment_data["text"]
    assert data["user"]== comment_data["user"]

def test_read_comment_by_id() -> None:
    """
    Test to retrieve a comment by its ID
    """
    response = client.get(f"{settings.API_V1_STR}/comments/{comment_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == comment_id
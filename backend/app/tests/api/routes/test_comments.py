from fastapi.testclient import TestClient
from sqlmodel import Session
from app.main import app
from app.core.config import settings
from app.models import CommentCreate, UserCreateOpen, Comment, UserTest
from app import crud
from app.tests.utils.utils import random_lower_string, random_email

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
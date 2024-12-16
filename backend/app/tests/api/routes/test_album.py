from fastapi.testclient import TestClient
from sqlmodel import Session
from app.main import app
from app.core.config import settings
from app.models import AlbumCreate, Album, UserTest
from app import crud
from app.tests.utils.utils import random_lower_string

client = TestClient(app)
album_id = 0

def test_read_albums() -> None:
    """
    Test to retrieve all albums.
    """
    response = client.get(f"{settings.API_V1_STR}/albums/")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert "count" in data
from fastapi.testclient import TestClient
from sqlmodel import Session
from app.main import app
from app.core.config import settings
from app.models import AlbumCreate, Album, UserTest
from app import crud
from datetime import datetime

client = TestClient(app)

def test_create_album_and_fail_to_create_duplicate() -> None:
    """
    Integration test to create an album and verify that trying to create a duplicate album fails.
    """
    album_data = {
        "title": "Duplicate Album",
        "artist": "Test Artist",
        "release_date": "2024-12-16",
        "genre": "Pop",
        "cover_image_url": "https://example.com/cover.jpg",
        "duration": 3600,
        "timestamp": datetime.utcnow().isoformat()
    }

    # 1. Crear un álbum
    create_response = client.post(f"{settings.API_V1_STR}/albums/", json=album_data)
    assert create_response.status_code == 200

    # 2. Intentar crear el mismo álbum de nuevo
    duplicate_response = client.post(f"{settings.API_V1_STR}/albums/", json=album_data)
    assert duplicate_response.status_code == 400

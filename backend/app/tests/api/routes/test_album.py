from fastapi.testclient import TestClient
from sqlmodel import Session
from app.main import app
from app.core.config import settings
from app.models import AlbumCreate, Album, UserTest
from app import crud
from app.tests.utils.utils import random_lower_string
from datetime import datetime

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

def test_create_album(client) -> None:
    """
    Test to create a new album.
    """
    album_data = {
        "title": "Album Test2",
        "artist": "Artist4",
        "release_date": "2024-12-16",
        "genre": "Pop",
        "cover_image_url": "https://example.com/cover.jpg",
        "duration": 3600,
        "timestamp": datetime.utcnow().isoformat()  # Fecha y hora actual en formato ISO
    }
    response = client.post(f"{settings.API_V1_STR}/albums/", json=album_data)
    print(response.json())  # Inspecciona el error devuelto por el servidor
    print("Response Status Code:", response.status_code)
    print("Response JSON:", response.json())
    assert response.status_code == 200
    data = response.json()
    global album_id
    album_id = data["id"]
    assert data["title"] == album_data["title"]
    assert data["artist"] == album_data["artist"]

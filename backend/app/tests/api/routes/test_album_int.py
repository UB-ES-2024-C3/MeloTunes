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

def test_create_and_read_album_by_id() -> None:
    """
    Integration test to create an album and read it by its ID.
    """
    # 1. Crear un álbum
    album_data = {
        "title": "Read Album",
        "artist": "Test Artist",
        "release_date": "2024-12-16",
        "genre": "Pop",
        "cover_image_url": "https://example.com/cover.jpg",
        "duration": 3600,
        "timestamp": datetime.utcnow().isoformat()
    }
    create_response = client.post(f"{settings.API_V1_STR}/albums/", json=album_data)
    assert create_response.status_code == 200

    album_id = create_response.json()["id"]

    # 2. Leer el álbum por su ID
    get_response = client.get(f"{settings.API_V1_STR}/albums/{album_id}")
    assert get_response.status_code == 200

    album = get_response.json()
    assert album["title"] == album_data["title"]

def test_create_user_and_create_album() -> None:
    """
    Integration test to create a user and then create an album with that user.
    """
    user_data = {
        "email": "artist9@example.com",
        "password": "Password123",
        "first_name": "Artist",
        "second_name": "One",
        "is_artist": True
    }

    # 1. Create user
    user_response = client.post(f"{settings.API_V1_STR}/users/", json=user_data)
    assert user_response.status_code == 200

    # 2. Authenticate user to get token
    login_response = client.post(f"{settings.API_V1_STR}/login/access-token", data={"username": user_data["email"], "password": user_data["password"]})
    assert login_response.status_code == 200
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 3. Create album
    album_data = {
        "title": "User Created Album",
        "artist": "Artist One",
        "release_date": "2024-12-16",
        "genre": "Pop",
        "cover_image_url": "https://example.com/cover.jpg",
        "duration": 3600,
        "timestamp": datetime.utcnow().isoformat()
    }
    album_response = client.post(f"{settings.API_V1_STR}/albums/", headers=headers, json=album_data)
    assert album_response.status_code == 200
    album_id = album_response.json()["id"]

    # 4. Delete album as the owner
    delete_response = client.delete(f"{settings.API_V1_STR}/albums/{album_id}", headers=headers)
    assert delete_response.status_code == 200

def test_create_and_read_album_by_title() -> None:
    """
    Integration test to create an album and then retrieve it by title.
    """
    album_data = {
        "title": "Test Create and Read",
        "artist": "Test Artist",
        "release_date": "2024-12-16",
        "genre": "Pop",
        "cover_image_url": "https://example.com/cover.jpg",
        "duration": 3600,
        "timestamp": datetime.utcnow().isoformat()
    }

    # Crear el álbum
    create_response = client.post(f"{settings.API_V1_STR}/albums/", json=album_data)
    assert create_response.status_code == 200

    album_title = album_data["title"]

    # Leer el álbum por su título
    get_response = client.get(f"{settings.API_V1_STR}/albums/albums/{album_title}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert len(data["data"]) > 0
    assert data["data"][0]["title"] == album_title

def test_create_album_with_missing_requirements() -> None:
    """
    Integration test to check if creating an album with missing requirements returns an error.
    """
    album_data = {
        "title": "Invalid Genre Integration Test",
        "artist": "Test Artist",
        "release_date": "2024-12-16",
        "genre": "Pop",
        "cover_image_url": "https://example.com/cover.jpg"
    }

    response = client.post(f"{settings.API_V1_STR}/albums/", json=album_data)

    assert response.status_code == 422
    data = response.json()
    assert "detail" in data

def test_create_and_delete_album_as_owner() -> None:
    """
    Integration test to create an album and then delete it as the owner (artist).
    """
    # Crear un artista
    artist_credentials = {"email": "owner@example.com", "password": "Password123"}
    client.post(f"{settings.API_V1_STR}/users/", json={
        "email": artist_credentials["email"],
        "password": artist_credentials["password"],
        "first_name": "Owner",
        "second_name": "Artist",
        "is_artist": True
    })

    # Hacer login como el artista
    login_response = client.post(f"{settings.API_V1_STR}/login/access-token", data={"username": artist_credentials["email"], "password": artist_credentials["password"]})
    assert login_response.status_code == 200
    artist_token = login_response.json()["access_token"]
    artist_headers = {"Authorization": f"Bearer {artist_token}"}

    # Crear un álbum como el artista
    album_data = {
        "title": "Album to Delete",
        "artist": "Owner Artist",
        "release_date": "2024-12-16",
        "genre": "Pop",
        "cover_image_url": "https://example.com/album_cover.jpg",
        "duration": 3600,
        "timestamp": datetime.utcnow().isoformat()
    }
    album_response = client.post(f"{settings.API_V1_STR}/albums/", headers=artist_headers, json=album_data)
    assert album_response.status_code == 200
    album_id = album_response.json()["id"]

    # Eliminar el álbum como el artista dueño
    delete_response = client.delete(f"{settings.API_V1_STR}/albums/{album_id}", headers=artist_headers)
    assert delete_response.status_code == 200

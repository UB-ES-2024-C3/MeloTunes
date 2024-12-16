from fastapi.testclient import TestClient
from sqlmodel import Session
from app.main import app
from app.core.config import settings
from app.models import AlbumCreate, Album, UserTest
from app import crud
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
        "title": "Test Album",
        "artist": "Artist",
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

def test_read_album_by_title() -> None:
    """
    Test to retrieve albums by title.
    """
    album_title_to_find = "Test Album"
    response = client.get(f"{settings.API_V1_STR}/albums/albums/{album_title_to_find}")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert len(data["data"]) > 0
    assert data["data"][0]["title"] == album_title_to_find

def test_delete_album_super_user(client: TestClient, db: Session) -> None:
    """
    Test to delete an album as a superuser.
    """
    # Crear un superusuario de prueba
    username = "test1@artist.com"
    password = "Superuser123"
    user_in = UserTest(email=username, password=password, first_name="Test Artist", second_name="Test Artist", is_superuser=True, is_artist=True)
    user = crud.user.create_user(session=db, user_create=user_in)

    # Hacer una solicitud POST a /login/access-token para obtener el token de acceso del nuevo usuario
    login_data = {
        "username": username,
        "password": password
    }
    login_response = client.post(f"{settings.API_V1_STR}/login/access-token", data=login_data)

    assert login_response.status_code == 200
    access_token = login_response.json()["access_token"]

    # Usamos el token generado para el nuevo usuario
    user_token_headers = {"Authorization": f"Bearer {access_token}"}

    # Intentar eliminar el álbum con el superusuario
    response = client.delete(
        f"{settings.API_V1_STR}/albums/{album_id}",
        headers=user_token_headers,
    )

    # Comprobamos que la eliminación fue exitosa
    assert response.status_code == 200
    deleted_album = response.json()
    assert deleted_album["message"] == "Album deleted successfully"

def test_create_album_already_exists(client) -> None:
    """
    Test to check if creating an album that already exists returns an error.
    """
    album_data = {
        "title": "Test Album",
        "artist": "Test Artist",
        "release_date": "2024-12-16",
        "genre": "Pop",
        "cover_image_url": "https://example.com/cover.jpg"
    }
    # Primero crea el álbum
    client.post(f"{settings.API_V1_STR}/albums/", json=album_data)

    # Ahora intenta crear el mismo álbum, debería fallar
    response = client.post(f"{settings.API_V1_STR}/albums/", json=album_data)
    assert response.status_code == 422
    data = response.json()

def test_read_album_by_title_not_found() -> None:
    """
    Test to check if album retrieval by title returns an empty list when no albums are found.
    """
    album_title_to_find = "Nonexistent Album"
    response = client.get(f"{settings.API_V1_STR}/albums/albums/{album_title_to_find}")
    assert response.status_code == 200
    data = response.json()
    assert len(data["data"]) == 0  # Verifica que no se encuentra ningún álbum
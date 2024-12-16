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

def test_delete_album_not_authorized(client: TestClient, db: Session) -> None:
    """
    Test to check if a non-authorized user cannot delete an album.
    """
    # Crear un usuario no autorizado (no es superusuario)
    username = "test2@artist.com"
    password = "User123"
    user_in = UserTest(email=username, password=password, first_name="Test Artist", second_name="Test Artist", is_superuser=False, is_artist=True)
    user = crud.user.create_user(session=db, user_create=user_in)

    # Hacer login con el nuevo usuario
    login_data = {"username": username, "password": password}
    login_response = client.post(f"{settings.API_V1_STR}/login/access-token", data=login_data)

    assert login_response.status_code == 200
    access_token = login_response.json()["access_token"]

    # Usamos el token del usuario no autorizado
    user_token_headers = {"Authorization": f"Bearer {access_token}"}

    # Intentar eliminar el álbum
    response = client.delete(f"{settings.API_V1_STR}/albums/{album_id}", headers=user_token_headers)

    # Verificar que no se permita la eliminación
    assert response.status_code == 404

def test_create_album_invalid_release_date(client) -> None:
    """
    Test to check if creating an album with an invalid release date format returns an error.
    """
    invalid_album_data = {
        "title": "Invalid Date Album",
        "artist": "Test Artist",
        "release_date": "16-12-2024",  # Fecha en formato incorrecto
        "genre": "Pop",
        "cover_image_url": "https://example.com/cover.jpg"
    }

    response = client.post(f"{settings.API_V1_STR}/albums/", json=invalid_album_data)

    assert response.status_code == 422  # 422 para errores de validación
    data = response.json()
    assert "detail" in data  # Detalles sobre el error de formato de fecha

def test_delete_album_not_found(client) -> None:
    """
    Test to check if trying to delete an album that doesn't exist returns a 404 error.
    """
    non_existent_album_id = 999999  # Un ID que no existe
    response = client.delete(f"{settings.API_V1_STR}/albums/{non_existent_album_id}")

    assert response.status_code == 404  # 404 para recursos no encontrados
    data = response.json()
    assert "detail" in data  # Detalles sobre el error de no encontrado

def test_create_album_missing_required_fields(client) -> None:
    """
    Test to check if creating an album with missing required fields returns an error.
    """
    album_data = {
        "artist": "Test Artist",
        "release_date": "2024-12-16",
    }
    # Falta el campo 'title', 'duration' y 'timestamp'
    response = client.post(f"{settings.API_V1_STR}/albums/", json=album_data)

    assert response.status_code == 422  # Error de validación
    data = response.json()
    assert "detail" in data  # Los detalles de los campos que faltan deben aparecer
    missing_fields = [error["loc"][-1] for error in data["detail"]]
    assert "title" in missing_fields
    assert "duration" in missing_fields
    assert "timestamp" in missing_fields

def test_create_album_with_invalid_genre(client) -> None:
    """
    Test to check if creating an album with an invalid genre returns an error.
    """
    album_data = {
        "title": "Invalid Genre Album",
        "artist": "Test Artist",
        "release_date": "2024-12-16",
        "genre": "Unknown Genre",  # Este género no está permitido
        "cover_image_url": "https://example.com/cover.jpg"
    }
    response = client.post(f"{settings.API_V1_STR}/albums/", json=album_data)

    assert response.status_code == 422  # Error de validación
    data = response.json()
    assert "detail" in data  # Debe mostrar el error de validación para el género

def test_filter_albums_by_genre(client) -> None:
    """
    Test to filter albums by genre.
    """
    genre = "Pop"
    response = client.get(f"{settings.API_V1_STR}/albums/?genre={genre}")

    assert response.status_code == 200
    data = response.json()

    for album in data["data"]:
        assert album["genre"] == genre  # Todos los álbumes deben tener el género solicitado

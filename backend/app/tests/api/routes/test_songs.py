from fastapi.testclient import TestClient
from sqlmodel import Session
from app.main import app
from app.core.config import settings
from app.models import SongCreate, UserCreateOpen, Song, UserTest
from app import crud
from app.tests.utils.utils import random_lower_string, random_email

client = TestClient(app)


def test_read_songs() -> None:
    """
    Test to retrieve all songs.
    """
    response = client.get(f"{settings.API_V1_STR}/songs/")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert "count" in data

from datetime import datetime, timedelta

def test_create_song(client):
    song_data = {
        "title": "Test Song",
        "artist": "Test Artist",
        "album": "Test Album",
        "duration": 360,  # Enviar duración en segundos
        "timestamp": datetime.utcnow().isoformat()  # Formato ISO 8601
    }
    response = client.post(f"{settings.API_V1_STR}/songs/", json=song_data)
    print(response.json())  # Inspecciona el error devuelto por el servidor
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == song_data["title"]
    assert data["artist"] == song_data["artist"]

    expected_duration = f"PT{song_data['duration'] // 60}M"
    assert data["duration"] == expected_duration

def test_read_song_by_id() -> None:
    """
    Test to retrieve a song by its ID.
    """
    song_id_to_find = 1 
    response = client.get(f"{settings.API_V1_STR}/songs/{song_id_to_find}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == song_id_to_find

def test_read_song_by_title() -> None:
    """
    Test to retrieve songs by their title.
    """
    song_title_to_find = "Tu jardín con enanitos" 
    response = client.get(f"{settings.API_V1_STR}/songs/songs/{song_title_to_find}")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert len(data["data"]) > 0
    assert data["data"][0]["title"] == song_title_to_find


def test_update_song(client, superuser_token_headers: dict[str, str]) -> None:
    """
    Test to update an existing song.
    """
    #title = "Test Song 2"
    #song_to_update = db.query(Song).filter(Song.title == title).first() 
    song_to_update = 1
    updated_data = {
        "title": "New Song",
        "artist": "New Artist",
        "album": "New Album",
        "duration": 360,  # Duración en segundos
        "timestamp": datetime.utcnow().isoformat()  # Formato ISO 8601
    }
    response = client.patch(
        f"{settings.API_V1_STR}/songs/{song_to_update}",
        headers=superuser_token_headers,
        json=updated_data,
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == updated_data["title"]
    assert data["artist"] == updated_data["artist"]

    # Convierte los segundos a formato ISO 8601 (duración en minutos)
    expected_duration = f"PT{updated_data['duration'] // 60}M"
    assert data["duration"] == expected_duration
    


def test_delete_song_super_user(
    client: TestClient, db: Session
) -> None:

    # Crear un superusuario de prueba
    username = "test1@artist.es"
    password = random_lower_string()
    user_in = UserTest(email=username, password=password, first_name="Test Artist", second_name="Test Artist", is_superuser=True, is_artist=True)
    user = crud.user.create_user(session=db, user_create=user_in)

        # Hacer una solicitud POST a /login/access-token para obtener el token de acceso del nuevo usuario
    login_data = {
        "username": username,
        "password": password
    }
    login_response = client.post(f"{settings.API_V1_STR}/login/access-token", data=login_data)
    
    # Verificamos que la solicitud para obtener el token fue exitosa
    assert login_response.status_code == 200
    access_token = login_response.json()["access_token"]
    
    # Usamos el token generado para el nuevo usuario
    user_token_headers = {"Authorization": f"Bearer {access_token}"}
    
    title = "Test Song"
    try:
        # Intentar obtener la canción de la base de datos
        song = db.query(Song).filter(Song.title == title).first() 
    except Exception as e:
        db.rollback()
        print(f"Error al obtener la canción: {e}")
        raise  # Rethrow the exception to stop the test
    song = db.query(Song).filter(Song.title == title).first() 
    
    # Intentar eliminar la canción con el superusuario
    r = client.delete(
        f"{settings.API_V1_STR}/songs/{song.id}",
        headers=user_token_headers,
    )
    
    # Comprobamos que la eliminación fue exitosa
    assert r.status_code == 200
    deleted_song = r.json()
    assert deleted_song["message"] == "Song deleted successfully"

from fastapi.testclient import TestClient
from sqlmodel import Session
from app.main import app
from app.core.config import settings
from app.models import SongCreate, UserCreateOpen, Song, UserTest
from app import crud
from app.tests.utils.utils import random_lower_string, random_email
from datetime import datetime

client = TestClient(app)

# Create and read song
def test_create_and_read_song_integration(client):
    """
    Integration test: Create a song and verify it can be retrieved by ID and title.
    """
    # Datos para crear la canción
    song_data = {
        "title": "Integration Test Song",
        "artist": "Integration Test Artist",
        "album": "Integration Test Album",
        "duration": 300,  # Enviar duración en segundos
        "timestamp": datetime.utcnow().isoformat()  # Formato ISO 8601
    }

    # Crear la canción
    create_response = client.post(f"{settings.API_V1_STR}/songs/", json=song_data)
    assert create_response.status_code == 200
    created_song = create_response.json()
    assert created_song["title"] == song_data["title"]

    # Recuperar la canción por ID
    song_id = created_song["id"]
    read_by_id_response = client.get(f"{settings.API_V1_STR}/songs/{song_id}")
    assert read_by_id_response.status_code == 200
    retrieved_song = read_by_id_response.json()
    assert retrieved_song["title"] == song_data["title"]

    # Recuperar la canción por título
    read_by_title_response = client.get(f"{settings.API_V1_STR}/songs/songs/{song_data['title']}")
    assert read_by_title_response.status_code == 200
    retrieved_songs_by_title = read_by_title_response.json()
    assert len(retrieved_songs_by_title["data"]) > 0
    assert retrieved_songs_by_title["data"][0]["title"] == song_data["title"]


# Create, edit and update song
def test_create_update_and_read_song_integration(client, superuser_token_headers):
    """
    Integration test: Create a song, update it, and verify the changes.
    """
    # Datos para crear la canción
    song_data = {
        "title": "Integration Update Song",
        "artist": "Original Artist",
        "album": "Original Album",
        "duration": 240,  # Duración en segundos
        "timestamp": datetime.utcnow().isoformat()
    }

    # Crear la canción
    create_response = client.post(f"{settings.API_V1_STR}/songs/", json=song_data)
    assert create_response.status_code == 200
    created_song = create_response.json()
    song_id = created_song["id"]

    # Datos para actualizar la canción
    updated_data = {
        "title": "Updated Song Title",
        "artist": "Updated Artist",
        "album": "Updated Album",
        "duration": 360,  # Duración en segundos
        "timestamp": datetime.utcnow().isoformat()
    }

    # Actualizar la canción
    update_response = client.patch(
        f"{settings.API_V1_STR}/songs/{song_id}",
        headers=superuser_token_headers,
        json=updated_data
    )
    assert update_response.status_code == 200
    updated_song = update_response.json()
    assert updated_song["title"] == updated_data["title"]

    # Recuperar la canción por ID para verificar los cambios
    read_by_id_response = client.get(f"{settings.API_V1_STR}/songs/{song_id}")
    assert read_by_id_response.status_code == 200
    retrieved_song = read_by_id_response.json()
    assert retrieved_song["title"] == updated_data["title"]

# Create user, create song and delete song
def test_user_create_song_and_delete_integration(client, db):
    """
    Integration test: Create a user, create a song, and delete the song.
    """
    # Crear un usuario
    user_data = {
        "email": random_email(),
        "password": random_lower_string(),
        "first_name": "Integration",
        "second_name": "User",
        "is_superuser": True
    }
    user = crud.user.create_user(session=db, user_create=UserTest(**user_data))

    # Obtener un token para el usuario
    login_response = client.post(f"{settings.API_V1_STR}/login/access-token", data={
        "username": user_data["email"],
        "password": user_data["password"]
    })
    assert login_response.status_code == 200
    access_token = login_response.json()["access_token"]
    token_headers = {"Authorization": f"Bearer {access_token}"}

    # Crear una canción
    song_data = {
        "title": "User Test Song",
        "artist": "User Artist",
        "album": "User Album",
        "duration": 210,
        "timestamp": datetime.utcnow().isoformat()
    }
    create_response = client.post(f"{settings.API_V1_STR}/songs/", json=song_data, headers=token_headers)
    assert create_response.status_code == 200
    created_song = create_response.json()
    song_id = created_song["id"]

    # Eliminar la canción
    delete_response = client.delete(f"{settings.API_V1_STR}/songs/{song_id}", headers=token_headers)
    assert delete_response.status_code == 200

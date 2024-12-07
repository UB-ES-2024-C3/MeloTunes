from fastapi.testclient import TestClient
from sqlmodel import Session
from app.main import app
from app.core.config import settings
from app.models import SongCreate, UserCreateOpen, Song, UserTest
from app import crud
from app.tests.utils.utils import random_lower_string, random_email
from datetime import datetime

client = TestClient(app)
user_token = " "
song_iden = " "

# Create, edit and update song
def test_user_create_song_add_to_favorites_and_check_in_favorites(client, db):
    """
    Integration test: Create a user, create a song, add the song to the user's favorites,
    and verify the song is in the favorites list.
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

    global user_token
    user_token = access_token

    token_headers = {"Authorization": f"Bearer {access_token}"}

    # Crear una canción
    song_data = {
        "title": "User Fav Song",
        "artist": "User Artist",
        "album": "User Album",
        "duration": 210,
        "timestamp": datetime.utcnow().isoformat()
    }
    create_response = client.post(f"{settings.API_V1_STR}/songs/", json=song_data, headers=token_headers)
    assert create_response.status_code == 200
    created_song = create_response.json()
    song_id = created_song["id"]

    global song_iden
    song_iden = song_id

    # Agregar la canción a la lista de favoritos del usuario
    add_fav_response = client.patch(
        f"{settings.API_V1_STR}/users/me/{song_id}",
        headers=token_headers
    )
    assert add_fav_response.status_code == 200

    # Obtener los favoritos del usuario y comprobar que la canción está en la lista
    favorites_response = client.get(f"{settings.API_V1_STR}/users/me/my_songs", headers=token_headers)
    assert favorites_response.status_code == 200
    favorites = favorites_response.json()

    # Verificar que la canción esté en la lista de favoritos
    assert any(fav["id"] == song_id for fav in favorites), "Song not found in favorites"


# Create, edit and update song
def test_remove_from_favorites(client, db):
    """
    Integration test: Create a user, create a song, add the song to the user's favorites,
    remove the song from the user's favorites, and verify the song is no longer in the favorites list.
    """
    # Crear un usuario
    token_headers = {"Authorization": f"Bearer {user_token}"}

    # Verificar que la canción esté en la lista de favoritos
    favorites_response = client.get(f"{settings.API_V1_STR}/users/me/my_songs", headers=token_headers)
    assert favorites_response.status_code == 200
    favorites = favorites_response.json()
    assert any(fav["id"] == song_iden for fav in favorites), "Song not found in favorites"

    # Eliminar la canción de la lista de favoritos del usuario
    remove_fav_response = client.patch(
        f"{settings.API_V1_STR}/users/me/my_songs/{song_iden}",
        headers=token_headers
    )
    assert remove_fav_response.status_code == 200

    # Verificar que la canción ya no esté en la lista de favoritos
    favorites_response_after_removal = client.get(f"{settings.API_V1_STR}/users/me/my_songs", headers=token_headers)
    assert favorites_response_after_removal.status_code == 200
    favorites_after_removal = favorites_response_after_removal.json()
    assert not any(fav["id"] == song_iden for fav in favorites_after_removal), "Song still found in favorites"

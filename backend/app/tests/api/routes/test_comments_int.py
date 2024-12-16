from fastapi.testclient import TestClient
from sqlmodel import Session
from app.main import app
from app.core.config import settings
from app.models import CommentCreate, UserCreateOpen, Comment, UserTest
from app import crud
from datetime import datetime

client = TestClient(app)

# Create and read comment
def test_create_and_read_comment_integration(client):
    """
    Integration test: Create a comment and verify it can be retrieved by ID.
    """
    # Datos para crear el comentario
    comment_data = {
        "text": "Integration Test Comment",
        "user": "Integration Test User",
        "song_id": 1,  # Asume que la canción con ID 1 ya existe
        "timestamp": datetime.utcnow().isoformat()
    }

    # Crear el comentario
    create_response = client.post(f"{settings.API_V1_STR}/comments/", json=comment_data)
    assert create_response.status_code == 200
    created_comment = create_response.json()
    assert created_comment["text"] == comment_data["text"]

    # Recuperar el comentario por ID
    comment_id = created_comment["id"]
    read_by_id_response = client.get(f"{settings.API_V1_STR}/comments/{comment_id}")
    assert read_by_id_response.status_code == 200
    retrieved_comment = read_by_id_response.json()
    assert retrieved_comment["text"] == comment_data["text"]

# Create and delete comment
def test_create_and_delete_comment_integration(client, superuser_token_headers):
    """
    Integration test: Create a comment and delete it.
    """
    # Datos para crear el comentario
    comment_data = {
        "text": "Integration Update Comment",
        "user": "Original User",
        "song_id": 1,
        "timestamp": datetime.utcnow().isoformat()
    }

    # Crear el comentario
    create_response = client.post(f"{settings.API_V1_STR}/comments/", json=comment_data)
    assert create_response.status_code == 200
    created_comment = create_response.json()
    comment_id = created_comment["id"]

    # Eliminar el comentario
    delete_response = client.delete(f"{settings.API_V1_STR}/comments/{comment_id}", headers=superuser_token_headers)
    assert delete_response.status_code == 200

# Trying to delete a comment with superuser
def test_delete_comment_with_multiple_users(client: TestClient, db: Session) -> None:
    """
    Integration test: Try to delete a comment with a superuser.
    """
    # Crear un comentario de prueba
    comment_data = {
        "text": "Test Comment Multiple Users",
        "user": "Test User",
        "song_id": 1,  # Asume que la canción con ID 1 ya existe
        "timestamp": "2023-01-01T00:00:00"
    }
    create_response = client.post(f"{settings.API_V1_STR}/comments/", json=comment_data)
    assert create_response.status_code == 200

    # Crear un superusuario
    user_data_super = {
        "email": "test_user_super@example.com",
        "first_name": "Test",
        "second_name": "UserSuper",
        "password": "Admin1234",
        "is_superuser": True,
        "is_artist": False
    }
    user_super = crud.user.create_user(session=db, user_create=UserTest(**user_data_super))

    # Eliminar el comentario con el superusuario
    delete_response_super = client.delete(
        f"{settings.API_V1_STR}/comments/{create_response.json()['id']}",
        headers={"Authorization": f"Bearer {user_super.id}"}
    )
    assert delete_response_super.status_code == 200  # El superusuario puede eliminar el comentario correctamente

# Create a comment with missing fields and check it doesn't post
def test_create_comment_missing_fields() -> None:
    """
    Test to check the behavior when creating a comment with missing fields.
    """
    comment_data = {
        "text": "Comentario con datos faltantes",
        "song_id": 1,  # Falta el campo 'user' y el 'timestamp'
    }
    response = client.post(f"{settings.API_V1_STR}/comments/", json=comment_data)
    assert response.status_code == 422  # 422 Unprocessable Entity
    data = response.json()
    assert "detail" in data  # Validar que hay un detalle del error
    assert "user" in data["detail"][0]["loc"]  # El error debe indicar que falta el 'user'
    assert "timestamp" not in data["detail"][0]["loc"]  # El error debe indicar que falta 'timestamp'

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
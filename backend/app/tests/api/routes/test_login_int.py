from fastapi.testclient import TestClient
from app.models import Token, UserCreate
from app import crud
from app.core.config import settings
from app.main import app

client = TestClient(app)

# Test de login
def test_login_endpoints(client, db) -> None:
    # Datos para la prueba
    email = "dianabrbr29@gmail.com"
    password = "TestPassword123"
    new_password = "NewTestPassword456"

    # Crear usuario de prueba
    user = crud.user.create_user(
        session=db,
        user_create=UserCreate(
            email=email,
            password=password,
            first_name="Test",
            second_name="User",
            is_active=True,
        ),
    )

    # Iniciar sesión con el usuario creado
    login_response = client.post(f"{settings.API_V1_STR}/login/access-token", data={
        "username": email,
        "password": password
    })
    assert login_response.status_code == 200
    token = login_response.json()

    assert "access_token" in token

    # Probar token de acceso
    test_token_response = client.post(
        f"{settings.API_V1_STR}/login/test-token",
        headers={"Authorization": f"Bearer {token['access_token']}"},
    )

    assert test_token_response.status_code == 200
    assert test_token_response.json()["email"] == email

    # Crear un superusuario para realizar la recuperación de contraseña
    superuser = crud.user.create_user(
        session=db,
        user_create=UserCreate(
            email="superuser@example.com",
            password="SuperuserPassword123",
            first_name="Super",
            second_name="User",
            is_active=True,
            is_superuser=True
        ),
    )
    superuser_token = client.post(
        f"{settings.API_V1_STR}/login/access-token",
        data={"username": superuser.email, "password": "SuperuserPassword123"},
    ).json()["access_token"]

    # Probar la recuperación de contraseña en formato HTML (requiere superusuario)
    recovery_html_response = client.post(
        f"{settings.API_V1_STR}/password-recovery-html-content/{email}",
        headers={"Authorization": f"Bearer {superuser_token}"},
    )
    
    # Comprobamos que la respuesta sea correcta
    assert recovery_html_response.status_code == 200
    assert "<html>" in recovery_html_response.text

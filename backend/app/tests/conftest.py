""" Tests configuration module """
from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, delete

from app.core.config import settings
import os
from app.core.db import engine, init_db
from app.main import app
from app.models import User
from app.tests.utils.user import authentication_token_from_email
from app.tests.utils.utils import get_superuser_token_headers
from pathlib import Path


@pytest.fixture(scope="session", autouse=True)
def db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        init_db(session)
        yield session
        statement = delete(User)
        session.execute(statement)
        session.commit()


@pytest.fixture(scope="module")
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="module")
def superuser_token_headers(client: TestClient) -> dict[str, str]:
    return get_superuser_token_headers(client)


@pytest.fixture(scope="module")
def normal_user_token_headers(client: TestClient, db: Session) -> dict[str, str]:
    return authentication_token_from_email(
        client=client, email=settings.EMAIL_TEST_USER, db=db
    )

from unittest.mock import patch

# Ruta donde debería estar el archivo en la estructura de directorios del proyecto
TEMPLATE_PATH = Path("app/email-templates/build")

@pytest.fixture(autouse=True)
def setup_email_template_path():
    # Crear la carpeta si no existe
    TEMPLATE_PATH.mkdir(parents=True, exist_ok=True)
    
    # Ruta del archivo de plantilla
    reset_password_path = TEMPLATE_PATH / "reset_password.html"
    
    # Crear el archivo si no existe
    if not reset_password_path.exists():
        with open(reset_password_path, "w") as f:
            f.write("<html><body><p>Reset Password Email Content</p></body></html>")
    
    # Asegurarse de que el archivo esté accesible
    yield
    
    # Limpiar después de la prueba (opcional)
    if reset_password_path.exists():
        os.remove(reset_password_path)
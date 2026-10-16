import uuid

from fastapi.testclient import TestClient

from app.core.config import settings
from tests.utils.utils import random_email, random_lower_string


def test_create_client(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    email = random_email()
    payload = {
        "external_id": "C-901",
        "full_name": "Comunidad Alfa",
        "email": email,
        "discord_username": "alfa#1234",
        "whatsapp_number": "573214118506",
    }
    r = client.post(
        f"{settings.API_V1_STR}/clients/",
        headers=superuser_token_headers,
        json=payload,
    )
    assert r.status_code == 200
    data = r.json()
    assert data["email"] == email
    assert data["full_name"] == "Comunidad Alfa"
    assert data["external_id"] == "C-901"
    assert data["whatsapp_number"] == "573214118506"
    assert "id" in data


def test_create_client_duplicate_email_returns_409(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    email = random_email()
    payload = {
        "full_name": "Cliente Original",
        "email": email,
        "whatsapp_number": "573001112233",
    }
    r1 = client.post(
        f"{settings.API_V1_STR}/clients/",
        headers=superuser_token_headers,
        json=payload,
    )
    assert r1.status_code == 200

    r2 = client.post(
        f"{settings.API_V1_STR}/clients/",
        headers=superuser_token_headers,
        json={"full_name": "Cliente Duplicado", "email": email},
    )
    assert r2.status_code == 409
    assert r2.json()["detail"] == "A client with this email already exists"


def test_read_and_update_client(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    email = random_email()
    create_res = client.post(
        f"{settings.API_V1_STR}/clients/",
        headers=superuser_token_headers,
        json={"full_name": "Before Update", "email": email},
    )
    assert create_res.status_code == 200
    client_id = create_res.json()["id"]

    get_res = client.get(
        f"{settings.API_V1_STR}/clients/{client_id}",
        headers=superuser_token_headers,
    )
    assert get_res.status_code == 200
    assert get_res.json()["full_name"] == "Before Update"

    update_res = client.put(
        f"{settings.API_V1_STR}/clients/{client_id}",
        headers=superuser_token_headers,
        json={"full_name": "After Update", "external_id": "C-UPD"},
    )
    assert update_res.status_code == 200
    assert update_res.json()["full_name"] == "After Update"
    assert update_res.json()["external_id"] == "C-UPD"

    list_res = client.get(
        f"{settings.API_V1_STR}/clients/",
        headers=superuser_token_headers,
    )
    assert list_res.status_code == 200
    assert list_res.json()["count"] >= 1


def test_read_client_not_found(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    r = client.get(
        f"{settings.API_V1_STR}/clients/{uuid.uuid4()}",
        headers=superuser_token_headers,
    )
    assert r.status_code == 404


def test_delete_client_cascades_servers(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    email = random_email()
    c_res = client.post(
        f"{settings.API_V1_STR}/clients/",
        headers=superuser_token_headers,
        json={"full_name": f"Cascade {random_lower_string()}", "email": email},
    )
    assert c_res.status_code == 200
    client_id = c_res.json()["id"]

    s_res = client.post(
        f"{settings.API_V1_STR}/servers/",
        headers=superuser_token_headers,
        json={
            "owner_id": client_id,
            "plan_name": "Plan 8GB",
            "game": "Minecraft",
            "status": "Activo",
        },
    )
    assert s_res.status_code == 200
    server_id = s_res.json()["id"]

    del_res = client.delete(
        f"{settings.API_V1_STR}/clients/{client_id}",
        headers=superuser_token_headers,
    )
    assert del_res.status_code == 200

    srv_check = client.get(
        f"{settings.API_V1_STR}/servers/{server_id}",
        headers=superuser_token_headers,
    )
    assert srv_check.status_code == 404


def test_clients_forbidden_for_normal_user(
    client: TestClient, normal_user_token_headers: dict[str, str]
) -> None:
    r = client.get(
        f"{settings.API_V1_STR}/clients/",
        headers=normal_user_token_headers,
    )
    assert r.status_code == 403

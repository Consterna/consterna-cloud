import uuid
from datetime import UTC, datetime, timedelta

from fastapi.testclient import TestClient

from app.core.config import settings
from tests.utils.utils import random_email


def _create_test_client(
    client: TestClient,
    superuser_token_headers: dict[str, str],
    name: str = "Test Gamer",
    phone: str = "573214118506",
) -> str:
    r = client.post(
        f"{settings.API_V1_STR}/clients/",
        headers=superuser_token_headers,
        json={
            "full_name": name,
            "email": random_email(),
            "whatsapp_number": phone,
        },
    )
    assert r.status_code == 200
    return str(r.json()["id"])


def test_create_server_with_crm_fields(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    owner_id = _create_test_client(client, superuser_token_headers, "Gamer Pro")
    exp = (datetime.now(UTC) + timedelta(days=20)).isoformat()
    payload = {
        "owner_id": owner_id,
        "ip_address": "172.93.100.10:25565",
        "plan_name": "Plan 12GB",
        "game": "Minecraft",
        "extra_service": "Creación de Modpack / Evento ($5 USD)",
        "currency": "USD",
        "monthly_price": 24.0,
        "one_time_fee": 5.0,
        "host_cost_usd": 12.0,
        "payment_method": "PayPal",
        "voice_port": "24454",
        "notes": "Modpack Cobblemon optimizado",
        "status": "Activo",
        "expiration_date": exp,
    }
    r = client.post(
        f"{settings.API_V1_STR}/servers/",
        headers=superuser_token_headers,
        json=payload,
    )
    assert r.status_code == 200
    data = r.json()
    assert data["game"] == "Minecraft"
    assert data["plan_name"] == "Plan 12GB"
    assert data["monthly_price"] == 24.0
    assert data["host_cost_usd"] == 12.0
    assert data["voice_port"] == "24454"


def test_create_server_nonexistent_owner_returns_404(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    r = client.post(
        f"{settings.API_V1_STR}/servers/",
        headers=superuser_token_headers,
        json={
            "owner_id": str(uuid.uuid4()),
            "plan_name": "Plan 4GB",
        },
    )
    assert r.status_code == 404


def test_read_expiring_servers(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    owner_id = _create_test_client(
        client, superuser_token_headers, "Cliente Renovación", "573214118506"
    )
    now = datetime.now(UTC)

    # 1. Expiring in 2 days (Active -> should appear)
    r_soon = client.post(
        f"{settings.API_V1_STR}/servers/",
        headers=superuser_token_headers,
        json={
            "owner_id": owner_id,
            "plan_name": "Plan 8GB",
            "game": "Project Zomboid",
            "currency": "COP",
            "monthly_price": 64000.0,
            "host_cost_usd": 8.0,
            "status": "Activo",
            "expiration_date": (now + timedelta(days=2)).isoformat(),
        },
    )
    assert r_soon.status_code == 200
    soon_id = r_soon.json()["id"]

    # 2. Overdue by 3 days (Active -> should appear)
    r_overdue = client.post(
        f"{settings.API_V1_STR}/servers/",
        headers=superuser_token_headers,
        json={
            "owner_id": owner_id,
            "plan_name": "Plan 6GB",
            "game": "Valheim",
            "currency": "USD",
            "monthly_price": 12.5,
            "host_cost_usd": 6.0,
            "status": "Activo",
            "expiration_date": (now - timedelta(days=3)).isoformat(),
        },
    )
    assert r_overdue.status_code == 200
    overdue_id = r_overdue.json()["id"]

    # 3. Expiring in 25 days (Active -> should NOT appear in days=4)
    r_far = client.post(
        f"{settings.API_V1_STR}/servers/",
        headers=superuser_token_headers,
        json={
            "owner_id": owner_id,
            "plan_name": "Plan 4GB",
            "game": "Terraria",
            "status": "Activo",
            "expiration_date": (now + timedelta(days=25)).isoformat(),
        },
    )
    assert r_far.status_code == 200
    far_id = r_far.json()["id"]

    # 4. Suspended server expiring tomorrow (Suspended -> should NOT appear)
    r_susp = client.post(
        f"{settings.API_V1_STR}/servers/",
        headers=superuser_token_headers,
        json={
            "owner_id": owner_id,
            "plan_name": "Plan 4GB",
            "game": "Rust",
            "status": "Suspendido",
            "expiration_date": (now + timedelta(days=1)).isoformat(),
        },
    )
    assert r_susp.status_code == 200
    susp_id = r_susp.json()["id"]

    exp_res = client.get(
        f"{settings.API_V1_STR}/servers/expiring?days=4",
        headers=superuser_token_headers,
    )
    assert exp_res.status_code == 200
    items = exp_res.json()
    returned_ids = {item["server_id"] for item in items}

    assert soon_id in returned_ids
    assert overdue_id in returned_ids
    assert far_id not in returned_ids
    assert susp_id not in returned_ids

    soon_entry = next(item for item in items if item["server_id"] == soon_id)
    assert soon_entry["whatsapp_url"].startswith("https://wa.me/573214118506?text=")
    assert "Project Zomboid" in soon_entry["reminder_message"]
    assert soon_entry["billing_status"] == "🟡 Cobrar Pronto"

    overdue_entry = next(item for item in items if item["server_id"] == overdue_id)
    assert overdue_entry["days_remaining"] < 0
    assert overdue_entry["billing_status"] == "🔴 Vencido"


def test_server_delivery_message(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    owner_id = _create_test_client(
        client, superuser_token_headers, "Clan Omega", "573009998877"
    )
    srv_res = client.post(
        f"{settings.API_V1_STR}/servers/",
        headers=superuser_token_headers,
        json={
            "owner_id": owner_id,
            "ip_address": "45.10.20.30:25565",
            "plan_name": "Plan 16GB",
            "game": "Minecraft",
            "voice_port": "24454",
            "status": "Activo",
            "expiration_date": (datetime.now(UTC) + timedelta(days=30)).isoformat(),
        },
    )
    assert srv_res.status_code == 200
    srv_id = srv_res.json()["id"]

    msg_res = client.get(
        f"{settings.API_V1_STR}/servers/{srv_id}/delivery-message",
        headers=superuser_token_headers,
    )
    assert msg_res.status_code == 200
    payload = msg_res.json()
    assert payload["server_id"] == srv_id
    assert payload["client_name"] == "Clan Omega"
    assert "45.10.20.30:25565" in payload["message"]
    assert "24454" in payload["message"]
    assert "panel.kinetichosting.net" in payload["message"]
    assert payload["whatsapp_url"].startswith("https://wa.me/573009998877?text=")

    not_found = client.get(
        f"{settings.API_V1_STR}/servers/{uuid.uuid4()}/delivery-message",
        headers=superuser_token_headers,
    )
    assert not_found.status_code == 404


def test_servers_summary_kpis_and_admin_ui(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    summary_res = client.get(
        f"{settings.API_V1_STR}/servers/summary",
        headers=superuser_token_headers,
    )
    assert summary_res.status_code == 200
    summary = summary_res.json()
    assert summary["total_clients"] >= 1
    assert summary["active_servers"] >= 1
    assert summary["mrr_usd_estimated"] > 0
    assert summary["host_cost_usd_total"] > 0
    assert summary["net_profit_usd"] == round(
        summary["mrr_usd_estimated"] - summary["host_cost_usd_total"], 2
    )
    assert summary["partner_split_50_50_usd"] == round(
        summary["net_profit_usd"] / 2.0, 2
    )

    admin_res = client.get("/admin")
    assert admin_res.status_code == 200
    assert "Consterna Cloud" in admin_res.text
    assert "División 50/50" in admin_res.text
    assert "Llave en Mano" in admin_res.text


def test_sync_excel_api_endpoint(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    res = client.post(
        f"{settings.API_V1_STR}/utils/sync-excel",
        headers=superuser_token_headers,
    )
    assert res.status_code == 200
    data = res.json()
    assert "clients_synced" in data
    assert "servers_synced" in data
    assert data["clients_synced"] >= 1
    assert data["servers_synced"] >= 1


def test_phone_colombian_normalization(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    owner_id = _create_test_client(
        client, superuser_token_headers, "Gamer Celular", "3214118506"
    )
    srv_res = client.post(
        f"{settings.API_V1_STR}/servers/",
        headers=superuser_token_headers,
        json={
            "owner_id": owner_id,
            "plan_name": "Plan 4GB",
            "game": "Minecraft",
            "status": "Activo",
        },
    )
    srv_id = srv_res.json()["id"]
    delivery_res = client.get(
        f"{settings.API_V1_STR}/servers/{srv_id}/delivery-message",
        headers=superuser_token_headers,
    )
    assert delivery_res.status_code == 200
    assert "https://wa.me/573214118506?text=" in delivery_res.json()["whatsapp_url"]


def test_voice_port_extraction_from_notes() -> None:
    from scripts.import_data import extract_voice_port

    assert extract_voice_port("Puerto de voz: 24454") == "24454"
    assert extract_voice_port("Configurado con Simple Voice Chat: 25570") == "25570"
    assert extract_voice_port("voice_port: 24460") == "24460"
    assert extract_voice_port("Sin notas especiales") is None


def test_multi_server_upsert_idempotent() -> None:
    import openpyxl
    from sqlalchemy.pool import StaticPool
    from sqlmodel import Session, SQLModel, create_engine, select

    from app.models import Client, Server
    from scripts.import_data import _sync_session

    temp_engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    SQLModel.metadata.create_all(temp_engine)

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "👥 Clientes Activos"
    # Row 1: Headers
    ws.append([
        "ID", "Nombre", "Tel", "Juego", "Extra", "Plan", "Moneda", "Precio",
        "ExtraFee", "Costo", "Ganancia", "Pago", "IP", "Inicio", "Dias",
        "Vence", "Aviso", "EstadoPago", "Estado", "WA", "Notas"
    ])
    # 2 servers for the same client with different IPs
    ws.append([
        "C-MULTI", "Multi Client", "573214118506", "Minecraft", "Ninguno (Solo Host)",
        "Plan 6GB", "USD", 12.5, 0, 6.0, 6.5, "PayPal", "10.0.0.1:25565", None, None,
        None, None, None, "Activo", None, "Puerto de voz: 24454"
    ])
    ws.append([
        "C-MULTI", "Multi Client", "573214118506", "Project Zomboid", "Ninguno (Solo Host)",
        "Plan 8GB", "USD", 16.0, 0, 8.0, 8.0, "PayPal", "10.0.0.2:16261", None, None,
        None, None, None, "Activo", None, None
    ])

    with Session(temp_engine) as session:
        res = _sync_session(ws, session)
        assert res["clients_synced"] == 2
        assert res["servers_synced"] == 2

        client_obj = session.exec(select(Client).where(Client.external_id == "C-MULTI")).first()
        assert client_obj is not None

        # Verify BOTH servers exist and neither was overwritten
        servers_list = session.exec(select(Server).where(Server.owner_id == client_obj.id)).all()
        assert len(servers_list) == 2
        ips = {s.ip_address for s in servers_list}
        assert "10.0.0.1:25565" in ips
        assert "10.0.0.2:16261" in ips

        mc = next(s for s in servers_list if s.ip_address == "10.0.0.1:25565")
        assert mc.voice_port == "24454"
        assert mc.game == "Minecraft"

        # Re-run _sync_session to prove idempotency (no duplicates)
        res2 = _sync_session(ws, session)
        assert res2["servers_synced"] == 2
        servers_list_after = session.exec(select(Server).where(Server.owner_id == client_obj.id)).all()
        assert len(servers_list_after) == 2

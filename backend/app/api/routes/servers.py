import re
import urllib.parse
import uuid
from datetime import UTC, datetime
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import col, func, select

from app.api.deps import SessionDep, get_current_active_superuser
from app.models import (
    Client,
    ExpiringServerPublic,
    Message,
    Server,
    ServerCreate,
    ServerDeliveryMessage,
    ServerPublic,
    ServersPublic,
    ServersSummary,
    ServerUpdate,
)

router = APIRouter(prefix="/servers", tags=["servers"])

ACTIVE_STATUSES = {"active", "activo", "🟢 encendido", "encendido"}
SUSPENDED_STATUSES = {"suspended", "suspendido", "🔴 apagado", "apagado"}
DEFAULT_TRM_COP = 4000.0
KINETIC_PANEL_URL = "https://panel.kinetichosting.net"


def is_server_active(status: str | None) -> bool:
    if not status:
        return False
    return status.strip().lower() in ACTIVE_STATUSES


def is_server_suspended(status: str | None) -> bool:
    if not status:
        return False
    return status.strip().lower() in SUSPENDED_STATUSES


def _clean_phone(phone: str | None) -> str:
    if not phone:
        return ""
    digits = re.sub(r"[^\d]", "", phone)
    if len(digits) == 10 and digits.startswith("3"):
        return f"57{digits}"
    return digits


def compute_days_remaining(expiration_date: datetime | None) -> int | None:
    if expiration_date is None:
        return None
    exp_utc = (
        expiration_date.astimezone(UTC)
        if expiration_date.tzinfo is not None
        else expiration_date.replace(tzinfo=UTC)
    )
    today_utc = datetime.now(UTC).date()
    return (exp_utc.date() - today_utc).days


def compute_billing_status(
    status: str | None, expiration_date: datetime | None, warning_days: int = 4
) -> str:
    if not is_server_active(status) or expiration_date is None:
        return "-"
    days_rem = compute_days_remaining(expiration_date)
    if days_rem is None:
        return "-"
    if days_rem < 0:
        return "🔴 Vencido"
    if days_rem <= warning_days:
        return "🟡 Cobrar Pronto"
    return "🟢 Al Día"


def build_renewal_whatsapp(
    client_name: str,
    phone: str | None,
    game: str,
    plan_name: str,
    monthly_price: float,
    currency: str,
    expiration_date: datetime | None,
) -> tuple[str, str]:
    date_str = (
        expiration_date.strftime("%d/%m/%Y")
        if expiration_date is not None
        else "próximamente"
    )
    price_str = (
        f"${int(monthly_price):,} COP".replace(",", ".")
        if currency.upper() == "COP"
        else f"${monthly_price:.2f} USD"
    )
    reminder_msg = (
        f"Hola {client_name}, te escribimos de Consterna Cloud ☁️. "
        f"Te recordamos que tu servidor de {game} ({plan_name}) tiene fecha de renovación el {date_str}. "
        f"El valor de tu mensualidad es de {price_str}. "
        f"¿Deseas realizar la renovación para mantener tu mundo activo sin interrupciones?"
    )
    clean_num = _clean_phone(phone)
    encoded = urllib.parse.quote(reminder_msg)
    return reminder_msg, f"https://wa.me/{clean_num}?text={encoded}"


def build_delivery_payload(server: Server, client: Client) -> ServerDeliveryMessage:
    renewal_str = (
        server.expiration_date.strftime("%d/%m/%Y")
        if server.expiration_date is not None
        else "A 30 días desde activación"
    )
    ip_str = server.ip_address or "Pendiente de asignación"
    voice_line = (
        f"\n🎙️ *Puerto Simple Voice Chat (UDP):* `{server.voice_port}`"
        if server.voice_port
        else ""
    )
    extra_line = (
        f"\n✨ *Servicio Adicional:* {server.extra_service}"
        if server.extra_service
        and server.extra_service != "Ninguno (Solo Host)"
        else ""
    )

    msg = (
        f"¡Hola {client.full_name}! 🎉 Tu servidor *Llave en Mano* de *Consterna Cloud* ☁️ ya está 100% configurado, pre-optimizado y en línea.\n\n"
        f"🎮 *Juego:* {server.game}\n"
        f"⚡ *Plan de RAM:* {server.plan_name}{extra_line}\n"
        f"🌐 *IP de Conexión:* `{ip_str}`{voice_line}\n"
        f"🖥️ *Panel de Control (Kinetic Panel):* {KINETIC_PANEL_URL}\n"
        f"📅 *Próxima Fecha de Corte:* {renewal_str}\n\n"
        f"✅ Incluye optimización anti-lag de ticks, copias de seguridad y soporte técnico directo en español. ¡Que disfrutes tu servidor!"
    )
    clean_num = _clean_phone(client.whatsapp_number)
    encoded = urllib.parse.quote(msg)
    wa_url = f"https://wa.me/{clean_num}?text={encoded}"

    return ServerDeliveryMessage(
        server_id=server.id,
        client_name=client.full_name,
        game=server.game,
        plan_name=server.plan_name,
        ip_address=server.ip_address,
        voice_port=server.voice_port,
        panel_url=KINETIC_PANEL_URL,
        renewal_date=renewal_str,
        message=msg,
        whatsapp_url=wa_url,
    )


@router.get(
    "/",
    dependencies=[Depends(get_current_active_superuser)],
    response_model=ServersPublic,
)
def read_servers(session: SessionDep, skip: int = 0, limit: int = 100) -> Any:
    """Retrieve servers."""
    count_statement = select(func.count()).select_from(Server)
    count = session.exec(count_statement).one()
    statement = (
        select(Server).order_by(col(Server.created_at).desc()).offset(skip).limit(limit)
    )
    servers = session.exec(statement).all()
    return ServersPublic(
        data=[ServerPublic.model_validate(s) for s in servers], count=count
    )


@router.get(
    "/expiring",
    dependencies=[Depends(get_current_active_superuser)],
    response_model=list[ExpiringServerPublic],
)
def read_expiring_servers(
    session: SessionDep,
    days: int = Query(default=4, ge=0, le=365),
) -> Any:
    """Return active servers expiring within `days` days (or already overdue)."""
    servers = session.exec(select(Server)).all()
    expiring_list: list[ExpiringServerPublic] = []

    for srv in servers:
        if not is_server_active(srv.status) or srv.expiration_date is None:
            continue
        days_rem = compute_days_remaining(srv.expiration_date)
        if days_rem is None or days_rem > days:
            continue

        client = session.get(Client, srv.owner_id)
        client_name = client.full_name if client else "Cliente"
        client_email = str(client.email) if client else "sin-correo@consterna.cloud"
        whatsapp_number = client.whatsapp_number if client else None

        reminder_msg, wa_url = build_renewal_whatsapp(
            client_name=client_name,
            phone=whatsapp_number,
            game=srv.game,
            plan_name=srv.plan_name,
            monthly_price=srv.monthly_price,
            currency=srv.currency,
            expiration_date=srv.expiration_date,
        )
        billing_status = compute_billing_status(
            srv.status, srv.expiration_date, warning_days=days
        )

        expiring_list.append(
            ExpiringServerPublic(
                id=srv.id,
                server_id=srv.id,
                owner_id=srv.owner_id,
                client_name=client_name,
                client_email=client_email,
                whatsapp_number=whatsapp_number,
                game=srv.game,
                plan_name=srv.plan_name,
                ip_address=srv.ip_address,
                currency=srv.currency,
                monthly_price=srv.monthly_price,
                status=srv.status,
                expiration_date=srv.expiration_date,
                renewal_date=srv.expiration_date.date().isoformat(),
                days_remaining=days_rem,
                billing_status=billing_status,
                reminder_message=reminder_msg,
                whatsapp_url=wa_url,
            )
        )

    expiring_list.sort(key=lambda item: item.days_remaining)
    return expiring_list


@router.get(
    "/summary",
    dependencies=[Depends(get_current_active_superuser)],
    response_model=ServersSummary,
)
def read_servers_summary(
    session: SessionDep,
    trm_cop: float = Query(default=DEFAULT_TRM_COP, gt=0),
) -> Any:
    """Return financial and operational KPIs across all clients and servers."""
    total_clients = session.exec(select(func.count()).select_from(Client)).one()
    servers = session.exec(select(Server)).all()

    total_servers = len(servers)
    active_count = 0
    suspended_count = 0
    expiring_soon_count = 0
    overdue_count = 0
    mrr_usd = 0.0
    host_cost_usd_total = 0.0
    one_time_usd_total = 0.0

    for srv in servers:
        curr = (srv.currency or "USD").upper()
        one_time_usd = (
            srv.one_time_fee / trm_cop if curr == "COP" else srv.one_time_fee
        )
        one_time_usd_total += one_time_usd

        if is_server_active(srv.status):
            active_count += 1
            monthly_usd = (
                srv.monthly_price / trm_cop if curr == "COP" else srv.monthly_price
            )
            mrr_usd += monthly_usd
            host_cost_usd_total += srv.host_cost_usd

            days_rem = compute_days_remaining(srv.expiration_date)
            if days_rem is not None:
                if days_rem < 0:
                    overdue_count += 1
                elif days_rem <= 4:
                    expiring_soon_count += 1
        elif is_server_suspended(srv.status):
            suspended_count += 1

    mrr_rounded = round(mrr_usd, 2)
    host_rounded = round(host_cost_usd_total, 2)
    net_profit = round(mrr_rounded - host_rounded, 2)
    partner_split = round(net_profit / 2.0, 2)

    return ServersSummary(
        total_clients=total_clients,
        total_servers=total_servers,
        active_servers=active_count,
        suspended_servers=suspended_count,
        expiring_soon_count=expiring_soon_count,
        overdue_count=overdue_count,
        trm_cop_usd=trm_cop,
        mrr_usd_estimated=mrr_rounded,
        host_cost_usd_total=host_rounded,
        one_time_fees_usd_total=round(one_time_usd_total, 2),
        net_profit_usd=net_profit,
        partner_split_50_50_usd=partner_split,
    )


@router.get(
    "/{id}/delivery-message",
    dependencies=[Depends(get_current_active_superuser)],
    response_model=ServerDeliveryMessage,
)
def get_server_delivery_message(session: SessionDep, id: uuid.UUID) -> Any:
    """Generate the turnkey ('Llave en Mano') delivery message for WhatsApp/Discord."""
    server = session.get(Server, id)
    if not server:
        raise HTTPException(status_code=404, detail="Server not found")
    client = session.get(Client, server.owner_id)
    if not client:
        raise HTTPException(status_code=404, detail="Owner client not found")
    return build_delivery_payload(server, client)


@router.get(
    "/{id}",
    dependencies=[Depends(get_current_active_superuser)],
    response_model=ServerPublic,
)
def read_server(session: SessionDep, id: uuid.UUID) -> Any:
    """Get server by ID."""
    server = session.get(Server, id)
    if not server:
        raise HTTPException(status_code=404, detail="Server not found")
    return server


@router.post(
    "/",
    dependencies=[Depends(get_current_active_superuser)],
    response_model=ServerPublic,
)
def create_server(*, session: SessionDep, server_in: ServerCreate) -> Any:
    """Create new server."""
    client = session.get(Client, server_in.owner_id)
    if not client:
        raise HTTPException(status_code=404, detail="Owner client not found")
    server = Server.model_validate(server_in)
    session.add(server)
    session.commit()
    session.refresh(server)
    return server


@router.put(
    "/{id}",
    dependencies=[Depends(get_current_active_superuser)],
    response_model=ServerPublic,
)
def update_server(
    *, session: SessionDep, id: uuid.UUID, server_in: ServerUpdate
) -> Any:
    """Update a server."""
    server = session.get(Server, id)
    if not server:
        raise HTTPException(status_code=404, detail="Server not found")
    update_dict = server_in.model_dump(exclude_unset=True)
    server.sqlmodel_update(update_dict)
    session.add(server)
    session.commit()
    session.refresh(server)
    return server


@router.delete("/{id}", dependencies=[Depends(get_current_active_superuser)])
def delete_server(session: SessionDep, id: uuid.UUID) -> Message:
    """Delete a server."""
    server = session.get(Server, id)
    if not server:
        raise HTTPException(status_code=404, detail="Server not found")
    session.delete(server)
    session.commit()
    return Message(message="Server deleted successfully")

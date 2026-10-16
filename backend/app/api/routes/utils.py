from typing import Any

from fastapi import APIRouter, Depends
from pydantic.networks import EmailStr

from app.api.deps import SessionDep, get_current_active_superuser
from app.models import Message
from app.utils import generate_test_email, send_email
from scripts.import_data import import_excel

router = APIRouter(prefix="/utils", tags=["utils"])


@router.post(
    "/test-email/",
    dependencies=[Depends(get_current_active_superuser)],
    status_code=201,
)
def test_email(email_to: EmailStr) -> Message:
    """
    Test emails.
    """
    email_data = generate_test_email(email_to=email_to)
    send_email(
        email_to=email_to,
        subject=email_data.subject,
        html_content=email_data.html_content,
    )
    return Message(message="Test email sent")


@router.post(
    "/sync-excel",
    dependencies=[Depends(get_current_active_superuser)],
)
def sync_excel_crm(session: SessionDep) -> dict[str, Any]:
    """Synchronize active clients and servers from the Excel CRM into the database."""
    result = import_excel(session=session)
    return {
        "message": (
            f"Sincronización completada ({result['clients_synced']} clientes, "
            f"{result['servers_synced']} servidores)."
        ),
        "clients_synced": result["clients_synced"],
        "servers_synced": result["servers_synced"],
    }


@router.get("/health-check/")
async def health_check() -> bool:
    return True

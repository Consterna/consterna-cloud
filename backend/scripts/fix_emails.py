import logging
import sys
from pathlib import Path

from sqlmodel import Session, select

BACKEND_DIR = Path(__file__).resolve().parents[1]
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from app.core.db import engine  # noqa: E402
from app.models import Client  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def fix_client_emails() -> int:
    """Reemplaza dominios legacy .local por .cloud para cumplir con EmailStr."""
    updated = 0
    with Session(engine) as session:
        clients = session.exec(select(Client)).all()
        for client in clients:
            if "consterna.local" in client.email:
                client.email = client.email.replace(
                    "consterna.local", "consterna.cloud"
                )
                session.add(client)
                updated += 1
        session.commit()
    logger.info("Correos actualizados de .local a .cloud: %d", updated)
    return updated


if __name__ == "__main__":
    fix_client_emails()

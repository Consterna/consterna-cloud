import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import pandas as pd
from sqlmodel import Session, select

BACKEND_DIR = Path(__file__).resolve().parents[1]
PROJECT_ROOT = BACKEND_DIR.parent
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from app.core.db import engine  # noqa: E402
from app.models import Client, Server  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def _clean_str(val: Any) -> str | None:
    if pd.isna(val):
        return None
    text = str(val).strip()
    return text if text and text.lower() != "nan" else None


def import_excel(excel_path: Path | None = None) -> None:
    target_path = (
        excel_path
        if excel_path is not None
        else PROJECT_ROOT / "Control_Clientes_Consterna_V7_ENTERPRISE.xlsx"
    )
    if not target_path.exists():
        logger.error("No se encontró el archivo Excel en: %s", target_path)
        return

    logger.info("Iniciando importación desde Excel: %s", target_path.name)
    df = pd.read_excel(target_path)

    with Session(engine) as session:
        for index, row in df.iterrows():
            raw_email = _clean_str(row.get("Email"))
            email = (
                raw_email
                if raw_email and "@" in raw_email
                else f"client_imported_{index}@consterna.cloud"
            )
            email = email.replace("@consterna.local", "@consterna.cloud")

            client = session.exec(select(Client).where(Client.email == email)).first()
            if not client:
                client = Client(
                    full_name=_clean_str(row.get("Nombre")) or "Desconocido",
                    email=email,
                    discord_username=_clean_str(row.get("Discord")),
                    whatsapp_number=_clean_str(row.get("WhatsApp")),
                )
                session.add(client)
                session.commit()
                session.refresh(client)
                logger.info("Creado cliente: %s", client.full_name)

            exp_raw = row.get("Fecha Vencimiento")
            exp_date: datetime | None = (
                None if pd.isna(exp_raw) else pd.to_datetime(exp_raw).to_pydatetime()
            )

            game_str = _clean_str(row.get("Juego")) or ""
            plan_str = _clean_str(row.get("Plan")) or ""
            plan_name = f"{game_str} - {plan_str}".strip(" -") or "Plan Base"
            status_val = (_clean_str(row.get("Estado")) or "pending").lower()

            server = Server(
                ip_address=_clean_str(row.get("IP")),
                plan_name=plan_name,
                status=status_val,
                expiration_date=exp_date,
                owner_id=client.id,
            )
            session.add(server)
            session.commit()
            logger.info("  -> Asignado servidor a %s (%s)", client.full_name, plan_name)

    logger.info("Importación completada con éxito.")


if __name__ == "__main__":
    import_excel()

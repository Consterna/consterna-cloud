import sqlite3
from typing import Any

from sqlalchemy import Engine, event, text
from sqlmodel import Session, SQLModel, create_engine, select

from app import crud
from app.core.config import settings
from app.models import User, UserCreate

engine = create_engine(str(settings.DATABASE_URL), pool_pre_ping=True)


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection: Any, _connection_record: Any) -> None:
    if isinstance(dbapi_connection, sqlite3.Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()


def _ensure_sqlite_columns(session: Session) -> None:
    bind = session.get_bind()
    if bind.dialect.name != "sqlite":
        return

    client_cols = {
        row[1]
        for row in session.execute(text("PRAGMA table_info(client)")).fetchall()
    }
    if client_cols and "external_id" not in client_cols:
        session.execute(
            text("ALTER TABLE client ADD COLUMN external_id VARCHAR(50)")
        )
        session.execute(
            text(
                "CREATE INDEX IF NOT EXISTS ix_client_external_id ON client (external_id)"
            )
        )

    server_cols = {
        row[1]
        for row in session.execute(text("PRAGMA table_info(server)")).fetchall()
    }
    if server_cols:
        migrations = [
            ("game", "VARCHAR(100) NOT NULL DEFAULT 'Minecraft'"),
            ("extra_service", "VARCHAR(150) NOT NULL DEFAULT 'Ninguno (Solo Host)'"),
            ("currency", "VARCHAR(10) NOT NULL DEFAULT 'USD'"),
            ("monthly_price", "FLOAT NOT NULL DEFAULT 0.0"),
            ("one_time_fee", "FLOAT NOT NULL DEFAULT 0.0"),
            ("host_cost_usd", "FLOAT NOT NULL DEFAULT 0.0"),
            ("payment_method", "VARCHAR(100)"),
            ("start_date", "DATE"),
            ("voice_port", "VARCHAR(50)"),
            ("notes", "VARCHAR(1000)"),
        ]
        for col_name, col_def in migrations:
            if col_name not in server_cols:
                session.execute(
                    text(f"ALTER TABLE server ADD COLUMN {col_name} {col_def}")
                )
    session.commit()


# make sure all SQLModel models are imported (app.models) before initializing DB
# otherwise, SQLModel might fail to initialize relationships properly
# for more details: https://github.com/fastapi/full-stack-fastapi-template/issues/28


def init_db(session: Session) -> None:
    # Ensure all SQLModel tables exist on the bound engine for this session
    SQLModel.metadata.create_all(session.get_bind())
    _ensure_sqlite_columns(session)

    user = session.exec(
        select(User).where(User.email == settings.FIRST_SUPERUSER)
    ).first()
    if not user:
        user_in = UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = crud.create_user(session=session, user_create=user_in)



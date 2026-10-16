import uuid
from datetime import UTC, date, datetime

from pydantic import EmailStr
from sqlalchemy import DateTime
from sqlmodel import Field, Relationship, SQLModel


def get_datetime_utc() -> datetime:
    return datetime.now(UTC)


# Shared properties
class UserBase(SQLModel):
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    is_active: bool = True
    is_superuser: bool = False
    full_name: str | None = Field(default=None, max_length=255)


# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=128)


class UserRegister(SQLModel):
    email: EmailStr = Field(max_length=255)
    password: str = Field(min_length=8, max_length=128)
    full_name: str | None = Field(default=None, max_length=255)


# Properties to receive via API on update, all are optional
class UserUpdate(SQLModel):
    email: EmailStr | None = Field(default=None, max_length=255)
    is_active: bool | None = None
    is_superuser: bool | None = None
    full_name: str | None = Field(default=None, max_length=255)
    password: str | None = Field(default=None, min_length=8, max_length=128)


class UserUpdateMe(SQLModel):
    full_name: str | None = Field(default=None, max_length=255)
    email: EmailStr | None = Field(default=None, max_length=255)


class UpdatePassword(SQLModel):
    current_password: str = Field(min_length=8, max_length=128)
    new_password: str = Field(min_length=8, max_length=128)


# Database model, database table inferred from class name
class User(UserBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    hashed_password: str
    created_at: datetime | None = Field(
        default_factory=get_datetime_utc,
        sa_type=DateTime(timezone=True),  # type: ignore
    )


# Properties to return via API, id is always required
class UserPublic(UserBase):
    id: uuid.UUID
    created_at: datetime | None = None


class UsersPublic(SQLModel):
    data: list[UserPublic]
    count: int


# --- CONSTERNA CLOUD BUSINESS MODELS ---


# Shared properties
class ClientBase(SQLModel):
    external_id: str | None = Field(default=None, max_length=50, index=True)
    full_name: str = Field(max_length=255)
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    discord_username: str | None = Field(default=None, max_length=255)
    whatsapp_number: str | None = Field(default=None, max_length=50)


class ClientCreate(ClientBase):
    pass


class ClientUpdate(SQLModel):
    external_id: str | None = Field(default=None, max_length=50)
    full_name: str | None = Field(default=None, max_length=255)
    email: EmailStr | None = Field(default=None, max_length=255)
    discord_username: str | None = Field(default=None, max_length=255)
    whatsapp_number: str | None = Field(default=None, max_length=50)


class Client(ClientBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime | None = Field(
        default_factory=get_datetime_utc,
        sa_type=DateTime(timezone=True),  # type: ignore
    )
    servers: list[Server] = Relationship(back_populates="owner", cascade_delete=True)


class ClientPublic(ClientBase):
    id: uuid.UUID
    created_at: datetime | None = None


class ClientsPublic(SQLModel):
    data: list[ClientPublic]
    count: int


# Shared properties
class ServerBase(SQLModel):
    ip_address: str | None = Field(default=None, max_length=255)
    plan_name: str = Field(max_length=255)
    game: str = Field(default="Minecraft", max_length=100)
    extra_service: str = Field(default="Ninguno (Solo Host)", max_length=150)
    currency: str = Field(default="USD", max_length=10)
    monthly_price: float = Field(default=0.0, ge=0)
    one_time_fee: float = Field(default=0.0, ge=0)
    host_cost_usd: float = Field(default=0.0, ge=0)
    payment_method: str | None = Field(default=None, max_length=100)
    start_date: date | None = Field(default=None)
    voice_port: str | None = Field(default=None, max_length=50)
    notes: str | None = Field(default=None, max_length=1000)
    status: str = Field(default="pending", max_length=50)  # pending, active, suspended
    expiration_date: datetime | None = Field(
        default=None, sa_type=DateTime(timezone=True)
    )  # type: ignore


class ServerCreate(ServerBase):
    owner_id: uuid.UUID


class ServerUpdate(SQLModel):
    ip_address: str | None = Field(default=None, max_length=255)
    plan_name: str | None = Field(default=None, max_length=255)
    game: str | None = Field(default=None, max_length=100)
    extra_service: str | None = Field(default=None, max_length=150)
    currency: str | None = Field(default=None, max_length=10)
    monthly_price: float | None = Field(default=None, ge=0)
    one_time_fee: float | None = Field(default=None, ge=0)
    host_cost_usd: float | None = Field(default=None, ge=0)
    payment_method: str | None = Field(default=None, max_length=100)
    start_date: date | None = Field(default=None)
    voice_port: str | None = Field(default=None, max_length=50)
    notes: str | None = Field(default=None, max_length=1000)
    status: str | None = Field(default=None, max_length=50)
    expiration_date: datetime | None = None


class Server(ServerBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime | None = Field(
        default_factory=get_datetime_utc,
        sa_type=DateTime(timezone=True),  # type: ignore
    )
    owner_id: uuid.UUID = Field(
        foreign_key="client.id", nullable=False, ondelete="CASCADE"
    )
    owner: Client | None = Relationship(back_populates="servers")


class ServerPublic(ServerBase):
    id: uuid.UUID
    owner_id: uuid.UUID
    created_at: datetime | None = None


class ServersPublic(SQLModel):
    data: list[ServerPublic]
    count: int


class ExpiringServerPublic(SQLModel):
    id: uuid.UUID
    server_id: uuid.UUID
    owner_id: uuid.UUID
    client_name: str
    client_email: str
    whatsapp_number: str | None = None
    game: str
    plan_name: str
    ip_address: str | None = None
    currency: str = "USD"
    monthly_price: float = 0.0
    status: str
    expiration_date: datetime | None = None
    renewal_date: str | None = None
    days_remaining: int
    billing_status: str
    reminder_message: str
    whatsapp_url: str


class ServerDeliveryMessage(SQLModel):
    server_id: uuid.UUID
    client_name: str
    game: str
    plan_name: str
    ip_address: str | None = None
    voice_port: str | None = None
    panel_url: str = "https://panel.kinetichosting.net"
    renewal_date: str | None = None
    message: str
    whatsapp_url: str


class ServersSummary(SQLModel):
    total_clients: int
    total_servers: int
    active_servers: int
    suspended_servers: int
    expiring_soon_count: int
    overdue_count: int
    trm_cop_usd: float = 4000.0
    mrr_usd_estimated: float
    host_cost_usd_total: float
    one_time_fees_usd_total: float
    net_profit_usd: float
    partner_split_50_50_usd: float


# Generic message
class Message(SQLModel):
    message: str


# JSON payload containing access token
class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"


# Contents of JWT token
class TokenPayload(SQLModel):
    sub: str | None = None


class NewPassword(SQLModel):
    token: str
    new_password: str = Field(min_length=8, max_length=128)

import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import col, func, select

from app.api.deps import SessionDep, get_current_active_superuser
from app.models import (
    Client,
    ClientCreate,
    ClientPublic,
    ClientsPublic,
    ClientUpdate,
    Message,
)

router = APIRouter(prefix="/clients", tags=["clients"])

@router.get("/", dependencies=[Depends(get_current_active_superuser)], response_model=ClientsPublic)
def read_clients(session: SessionDep, skip: int = 0, limit: int = 100) -> Any:
    """Retrieve clients."""
    count_statement = select(func.count()).select_from(Client)
    count = session.exec(count_statement).one()
    statement = select(Client).order_by(col(Client.created_at).desc()).offset(skip).limit(limit)
    clients = session.exec(statement).all()
    return ClientsPublic(data=[ClientPublic.model_validate(c) for c in clients], count=count)

@router.get("/{id}", dependencies=[Depends(get_current_active_superuser)], response_model=ClientPublic)
def read_client(session: SessionDep, id: uuid.UUID) -> Any:
    """Get client by ID."""
    client = session.get(Client, id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@router.post("/", dependencies=[Depends(get_current_active_superuser)], response_model=ClientPublic)
def create_client(*, session: SessionDep, client_in: ClientCreate) -> Any:
    """Create new client."""
    # Check if email exists
    existing = session.exec(select(Client).where(Client.email == client_in.email)).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered for a client")

    client = Client.model_validate(client_in)
    session.add(client)
    session.commit()
    session.refresh(client)
    return client

@router.put("/{id}", dependencies=[Depends(get_current_active_superuser)], response_model=ClientPublic)
def update_client(*, session: SessionDep, id: uuid.UUID, client_in: ClientUpdate) -> Any:
    """Update a client."""
    client = session.get(Client, id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    update_dict = client_in.model_dump(exclude_unset=True)
    client.sqlmodel_update(update_dict)
    session.add(client)
    session.commit()
    session.refresh(client)
    return client

@router.delete("/{id}", dependencies=[Depends(get_current_active_superuser)])
def delete_client(session: SessionDep, id: uuid.UUID) -> Message:
    """Delete a client."""
    client = session.get(Client, id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    session.delete(client)
    session.commit()
    return Message(message="Client deleted successfully")

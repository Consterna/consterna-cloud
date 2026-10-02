import uuid
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import col, func, select

from app.api.deps import CurrentUser, SessionDep, get_current_active_superuser
from app.models import Server, ServerCreate, ServerPublic, ServersPublic, ServerUpdate, Message, Client

router = APIRouter(prefix="/servers", tags=["servers"])

@router.get("/", dependencies=[Depends(get_current_active_superuser)], response_model=ServersPublic)
def read_servers(session: SessionDep, skip: int = 0, limit: int = 100) -> Any:
    """Retrieve servers."""
    count_statement = select(func.count()).select_from(Server)
    count = session.exec(count_statement).one()
    statement = select(Server).order_by(col(Server.created_at).desc()).offset(skip).limit(limit)
    servers = session.exec(statement).all()
    return ServersPublic(data=[ServerPublic.model_validate(s) for s in servers], count=count)

@router.get("/{id}", dependencies=[Depends(get_current_active_superuser)], response_model=ServerPublic)
def read_server(session: SessionDep, id: uuid.UUID) -> Any:
    """Get server by ID."""
    server = session.get(Server, id)
    if not server:
        raise HTTPException(status_code=404, detail="Server not found")
    return server

@router.post("/", dependencies=[Depends(get_current_active_superuser)], response_model=ServerPublic)
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

@router.put("/{id}", dependencies=[Depends(get_current_active_superuser)], response_model=ServerPublic)
def update_server(*, session: SessionDep, id: uuid.UUID, server_in: ServerUpdate) -> Any:
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

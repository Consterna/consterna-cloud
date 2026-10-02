from sqlmodel import Session, select
from app.core.db import engine
from app.models import Client
with Session(engine) as session:
    clients = session.exec(select(Client)).all()
    for c in clients:
        if 'consterna.local' in c.email:
            c.email = c.email.replace('consterna.local', 'consterna.cloud')
            session.add(c)
    session.commit()

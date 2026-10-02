import pandas as pd
from sqlmodel import Session, select
from app.core.db import engine
from app.models import Client, Server
import math

def import_excel():
    print("Iniciando importación desde Excel...")
    df = pd.read_excel('../Control_Clientes_Consterna_V7_ENTERPRISE.xlsx')
    
    with Session(engine) as session:
        for index, row in df.iterrows():
            email = str(row.get('Email', '')).strip()
            if email == 'nan' or not email:
                email = f"client_imported_{index}@consterna.local"
                
            # Handle possible NaNs in string columns
            def get_str(val):
                if pd.isna(val):
                    return None
                return str(val).strip()

            # Create or update Client
            client = session.exec(select(Client).where(Client.email == email)).first()
            if not client:
                client = Client(
                    full_name=get_str(row.get('Nombre')) or "Desconocido",
                    email=email,
                    discord_username=get_str(row.get('Discord')),
                    whatsapp_number=get_str(row.get('WhatsApp')),
                )
                session.add(client)
                session.commit()
                session.refresh(client)
                print(f"Creado cliente: {client.full_name}")
            
            # Create Server
            exp_date = row.get('Fecha Vencimiento')
            if pd.isna(exp_date):
                exp_date = None
            else:
                exp_date = pd.to_datetime(exp_date).to_pydatetime()
                
            plan_name = f"{get_str(row.get('Juego', ''))} - {get_str(row.get('Plan', ''))}"
            status_val = get_str(row.get('Estado'))
            if status_val:
                status_val = status_val.lower()
            else:
                status_val = "pending"
            
            server = Server(
                ip_address=get_str(row.get('IP')),
                plan_name=plan_name,
                status=status_val,
                expiration_date=exp_date,
                owner_id=client.id
            )
            session.add(server)
            session.commit()
            print(f"  -> Asignado servidor a {client.full_name} ({plan_name})")

    print("Importación completada con éxito.")

if __name__ == "__main__":
    import_excel()

# ☁️ Consterna Cloud - Backend API (FastAPI + SQLModel + Alembic)

API Backend para la gestión de clientes, servidores, planes y autenticación de **Consterna Cloud**, construida con **FastAPI**, **SQLModel**, **Pydantic v2** y **Alembic**.

---

## 📋 Requisitos

* [Python 3.14+](https://www.python.org/) (o entorno virtual local en `./venv`)
* [uv](https://docs.astral.sh/uv/) o `pip` para gestión de paquetes y entorno virtual
* [Docker](https://www.docker.com/) (opcional, para despliegue con PostgreSQL y Traefik vía `compose.yml`)

---

## 🚀 Desarrollo Local (Windows / PowerShell)

Desde el directorio `./backend/`, activa o utiliza el entorno virtual local:

```powershell
# Ejecutar migraciones de base de datos (Alembic)
.\venv\Scripts\python -m alembic upgrade head

# Levantar el servidor de desarrollo en http://127.0.0.1:8000
.\venv\Scripts\python -m uvicorn app.main:app --port 8000 --host 127.0.0.1 --reload
```

La API estará disponible en `http://localhost:8000`, con documentación interactiva automática:
* **Swagger UI:** `http://localhost:8000/docs`
* **ReDoc:** `http://localhost:8000/redoc`

---

## 🏗️ Estructura del Backend (`./backend/`)

* `app/main.py`: Punto de entrada de la aplicación FastAPI y configuración CORS/Rutas.
* `app/models.py`: Modelos de datos y tablas `SQLModel` (`User`, `Client`, `Server`) con validación estricta y borrado en cascada (`cascade_delete=True`).
* `app/crud.py`: Operaciones CRUD reutilizables sobre la base de datos.
* `app/api/routes/`: Endpoints REST (`/api/v1/login`, `/api/v1/users`, `/api/v1/clients`, `/api/v1/servers`, `/api/v1/utils`, `/api/v1/private`).
* `app/core/`: Configuración central (`config.py` leyendo `../.env`), conexión a base de datos (`db.py`) y seguridad JWT/Argon2 (`security.py`).
* `app/alembic/`: Entorno y versiones de migraciones de esquema de base de datos (`versions/0794bc9fbf9f_initial_schema.py`).
* `scripts/`: Scripts de utilidad para pre-arranque, pruebas, formateo (`ruff`), tipado (`mypy`) y migración/saneamiento de datos (`import_data.py`, `fix_emails.py`).
* `tests/`: Suite de 47 pruebas automatizadas con `pytest` (`api/`, `crud/`, `scripts/`, `utils/`).

---

## 🧪 Calidad de Código y Pruebas (`Pytest`, `Ruff`, `Mypy`)

Desde el directorio `./backend/`:

```powershell
# 1. Linter y formato (Ruff)
.\venv\Scripts\ruff check . --fix

# 2. Verificación estricta de tipos (Mypy)
.\venv\Scripts\mypy .

# 3. Suite completa de pruebas unitarias e integración (47 tests)
.\venv\Scripts\pytest
```

---

## 🗄️ Migraciones de Base de Datos (Alembic)

El entorno de desarrollo utiliza **SQLite** (`consterna.db`, ignorado en Git) y está preparado para **PostgreSQL** en producción.

1. Tras modificar modelos en `app/models.py`, genera una nueva revisión desde `./backend/`:
   ```powershell
   .\venv\Scripts\python -m alembic revision --autogenerate -m "Descripción del cambio"
   ```
2. Aplica la migración a la base de datos:
   ```powershell
   .\venv\Scripts\python -m alembic upgrade head
   ```

---

## 📈 Avances Backend (Octubre 2026)

- Base de datos conectada con SQLite (listo para PostgreSQL).
- Validadores estrictos (`Pydantic EmailStr` y `UUID`) corregidos.
- Entorno Alembic iniciado (`0794bc9fbf9f_initial_schema.py`).
- Pruebas E2E y unitarias exitosas (47/47 pasando — CRUD Usuarios/Clientes/Servidores).
- Siguiente paso: Panel Administrativo Frontend.


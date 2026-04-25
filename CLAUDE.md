# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

**Run the application:**
```bash
python run.py
```
Server starts at `http://0.0.0.0:3001` with auto-reload.

**Install dependencies (Pipenv preferred, Python 3.12):**
```bash
pipenv install
# or
pip install -r requirements.txt
```

**Run tests:**
```bash
pytest -s -v src/models/settings/database_connection_handler_test.py
pytest -s -v src/models/repositories/users_repository_test.py
```

**Lint:**
```bash
pylint <file>
```

## Architecture

The project uses a layered **Repository Pattern** with async/await throughout.

```
run.py                              → Uvicorn entry point (port 3001)
src/main/server/server.py           → FastAPI app, router registration
src/main/routes/users_routes.py     → APIRouter endpoints (tagged "Users")
src/models/repositories/            → Data access layer (Repository classes)
src/models/entities/                → SQLAlchemy Table definitions (Core, not ORM)
src/models/settings/                → DB engine, session factory, metadata
init/schema.sql                     → Initial SQLite schema
schema.db                           → SQLite database file (runtime artifact)
```

**Database:** SQLite via `aiosqlite` (`sqlite+aiosqlite:///schema.db`). The engine is configured with pool size 2, max overflow 0, timeout 30s. Sessions are managed through `DBConnectionHandler`, an async context manager in `src/models/settings/database_connection_handler.py`.

**Repository classes** (e.g., `UsersRepository`) use SQLAlchemy Core (not ORM), accept plain dicts, and operate inside async `with DBConnectionHandler() as session:` blocks.

**Tests** live alongside the source files they test (`_test.py` suffix). Async tests use `@pytest.mark.asyncio`. Integration tests that touch the real database are currently marked `@pytest.mark.skip`.

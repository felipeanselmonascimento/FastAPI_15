# string de conexao -> aonde esta o banco de onde esta as credenciais

from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

CONNECTION_STRING = "sqlite+aiosqlite:///schema.db"

engine = create_async_engine(
    CONNECTION_STRING,
    echo=False,
    pool_size=2,
    max_overflow=0,
    pool_timeout=30
)

#  se quiser ver as logs colocar isso para true   echo=False

# nao criar mais de duas conexoes com nosso banco de dados   pool_size=2,

# pra nao criar mais de nenhum tipo de conexao max_overflow=0,

# pra nao ficar com conexoes batendo no banco de persistindo la pool_timeout=30

async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
# entro no banco, crio uma sessao, depois saiu do banco falando q ta tudo certinho

class DBConnectionHandler:
    def __init__(self) -> None:
        self.session: Optional[AsyncSession] = None

    async def __aenter__(self):
        self.session = async_session()
        # só cria o objeto, sem IO
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()
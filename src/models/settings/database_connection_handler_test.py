import pytest
from .database_connection_handler import DBConnectionHandler


@pytest.mark.asyncio
@pytest.mark.skip(reason="Connecting with DB")
async def test_connection():
    async with DBConnectionHandler() as db_handler:
        assert db_handler.session is not None
#         // JavaScript - Jest
# expect(dbHandler.session).not.toBeNull()

# sempre colocar test_ na frente de toda funcao de teste q definirmos

# pytest -s -v src/models/settings/users_repository_test.py

# .mark.asyncio é necessário porque o pytest é síncrono por padrão, e o decorator avisa que precisa de tratamento especial pra rodar código async.
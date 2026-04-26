import pytest
from .users_repository import UsersRepository

@pytest.mark.asyncio
@pytest.mark.skip(reason="Insert in DB")
async def test_insert_user():
    new_user = {
        "user_name": "NomeDeTeste",
        "age": 99,
        "uf": "SP"
    }
    repo = UsersRepository()
    await repo.insert_users(new_user)

@pytest.mark.asyncio
@pytest.mark.skip(reason="Update in DB")
async def test_update_user():
    updated_infos = {
        "user_name": "NomeAtualizado",
        "age": 30,
        "uf": "RJ"
    }
    repo = UsersRepository()
    await repo.update_user(1, updated_infos)

    # pytest -s -v src/models/repositories/users_repository_test.py

# @pytest.mark.skip(reason="Insert in DB")
@pytest.mark.asyncio
async def test_get_users_by_id():
    repo = UsersRepository()
    response = await repo.get_users_by_id(1)
    print(response)
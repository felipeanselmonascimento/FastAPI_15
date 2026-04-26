from sqlalchemy import insert, update, select
from src.models.entities.users import Users
from src.models.settings.database_connection_handler import DBConnectionHandler
from .interfaces.users_repository import UsersRepositoryInterface


class UsersRepository(UsersRepositoryInterface):
    async def insert_users(self, user_infos: dict) -> None:
        async with DBConnectionHandler() as db:
            query = insert(Users).values(**user_infos)
            await db.session.execute(query)
            await db.session.commit()

            # O ** "desempacota" o dicionário — é igual o spread do JS:

            # dict É igual ao objeto do JS!

    async def update_user(self, user_id: int, user_infos: dict) -> None:
        async with DBConnectionHandler() as db:
            query = update(Users).where(Users.c.id == user_id).values(**user_infos)
            await db.session.execute(query)
            await db.session.commit()  # ← commit so pra quando modifica algo no banco

    async def get_users_by_id(self, user_id: int) -> list[dict]:
        async with DBConnectionHandler() as db:
            query = select(Users).where(Users.c.id == user_id)
            result = await db.session.execute(query)
            rows = result.fetchall()
            users_list = [dict(row._mapping) for row in rows]
            return users_list
        
        # O .c é um atalho para columns — as colunas da tabela.


# users_list = [dict(row._mapping) for row in rows]

# # resultado
# [
#     {"id": 1, "user_name": "felipe", "age": 20, "uf": "SP"},
#     {"id": 2, "user_name": "joao",   "age": 25, "uf": "RJ"},
# ]
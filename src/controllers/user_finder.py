from src.models.repositories.interfaces.users_repository import UsersRepositoryInterface


class UserFinder:
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    async def get_users_by_id(self, user_id: int) -> dict:
        users = await self.__users_repository.get_users_by_id(user_id)
        return {
            "type": "USERS",
            "count": len(users),
            "atributtes": users
        }
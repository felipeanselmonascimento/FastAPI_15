from abc import ABC, abstractmethod

class UsersRepositoryInterface(ABC):
    @abstractmethod
    async def insert_users(self, user_infos: dict) -> None: pass
    @abstractmethod
    async def update_user(self, user_id: int, user_infos: dict) -> None: pass
    @abstractmethod
    async def get_users_by_id(self, user_id: int) -> list[dict]: pass
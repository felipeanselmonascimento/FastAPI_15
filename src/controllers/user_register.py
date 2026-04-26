from src.models.repositories.interfaces.users_repository import UsersRepositoryInterface

class UserRegister:
    def __init__(self, user_repository: UsersRepositoryInterface) -> None:
        self.user_repository = user_repository
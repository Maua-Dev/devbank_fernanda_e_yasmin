from typing import List
from src.app.repo.user_repo_interface import IUserRepository
from ..entities.user import User


class UserRepositoryMock(IUserRepository):
    def __init__(self):
        user : User
        self.user=User(name= "Fernanda", agency="1234", account="12345-6", current_balance=8000.0)

    def get_user(self) -> List(User):
        return self.user


from abc import ABC, abstractmethod
from typing import List
from ..entities.user import User

class IUserRepository(ABC):
    @abstractmethod
    def get_user(self) -> List[User]:
        pass


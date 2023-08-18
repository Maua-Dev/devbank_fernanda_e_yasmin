from abc import ABC, abstractmethod
from typing import List
from ..entities.transactions import Transactions

class ITransactionsRepository(ABC):
    @abstractmethod
    def get_transaction_type(self) -> List[Transactions]:
        pass

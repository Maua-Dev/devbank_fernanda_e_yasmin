from typing import Dict, Optional, List

from ..entities.transactions import Transactions
from ..repo.transaction_repo_interface import ITransactionsRepository
from ..enums.transaction_type_enum import TRANSACTION_TYPE_ENUM
from ..entities.user import User
from ..repo.user_repository_mock import UserRepositoryMock
import time


class TransactionRepositoryMock(ITransactionsRepository):
    transactions: Dict[int, Transactions]
    
    def __init__(self):
        user = UserRepositoryMock.get_user()

        self.transactions = {
            1: Transactions(transaction_type= TRANSACTION_TYPE_ENUM.WITHDRAW, current_balance= user.current_balance, timestamp= time.time()),
            2: Transactions(transaction_type= TRANSACTION_TYPE_ENUM.DEPOSIT, current_balance= user.current_balance, timestamp= time.time()),
        }
        
    def get_all_items(self) -> List[Transactions]:
        return self.items.values()
    
    def get_transaction_type(self) -> List[Transactions]:
        return self.transactions[1].transaction_type, self.transactions[2].transaction_type
    
    
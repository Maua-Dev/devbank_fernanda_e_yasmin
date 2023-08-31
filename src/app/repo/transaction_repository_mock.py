from typing import List
from src.app.repo.transaction_repo_interface import ITransactionsRepository
from src.app.enums.transaction_type_enum import TRANSACTION_TYPE


class TransactionRepositoryMock(ITransactionsRepository):
    transaction : Transaction

    def __ini__(self):
        self.transaction=Transaction()

    def create_transaction(self, transaction: Transaction = None) -> List[str, float]:
        if transaction.type == TRANSACTION_TYPE.DEPOSIT:
            transaction.current_balance = transaction.current_balance + transaction.value
        elif transaction.type == TRANSACTION_TYPE.WITHDRAW:
            transaction.current_balance = transaction.current_balance - transaction.value

        transaction = Transaction(
            type_transactions=transaction.type,
            value=transaction.value,
            current_balance=transaction.current_balance
        )

    
    
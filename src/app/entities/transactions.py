from typing import Tuple
from ..enums.transaction_type_enum import TransactionTypeEnum
from ..errors.entity_errors import ParamNotValidated

import datetime

class Transactions:
    transaction_type: TransactionTypeEnum
    current_balance: float
    timestamp: float

    def __init__(self, transaction_type= None, current_balance= 0, timestamp=0):
        validation_transaction_type = self.validate_transaction_type(transaction_type)
        if transaction_type[0] is False:
            raise ParamNotValidated("transaction_type", validation_transaction_type[1])
        self.transaction_type = transaction_type

        validation_current_balance = self.validate_current_balance(current_balance)
        if current_balance[0] is False:
            raise ParamNotValidated("current_balance", validation_current_balance[1])
        self.current_balance = current_balance

        validation_timestamp = self.validate_timestamp(timestamp)
        if timestamp[0] is False:
            raise ParamNotValidated("timestamp", validation_timestamp[1])
        self.timestamp = timestamp

    @staticmethod
    def validate_transaction_type(transaction_type: TransactionTypeEnum) -> Tuple[bool, str]:
        if transaction_type is None:
            return (False, "transaction type is required")
        if type(transaction_type) != TransactionTypeEnum:
            return (False, "transaction_type must be a TransactionTypeEnum")
        return (True, "")

    @staticmethod
    def validate_current_balance(current_balance: float) -> Tuple[bool, str]:
        if type(current_balance) != float:
            return (False, "current balance must be a float")
        if current_balance < 0:
            return (False, "current balance must be positive")
        return (True, "")

    @staticmethod
    def validate_timestamp(timestamp: float) -> Tuple[bool, str]:
        if timestamp is None:
            return (False, "timestamp must be valid")
        if timestamp != float:
            return (False, "timestamp must be a float")
        return (True, "")

    def to_dict(self):
            return {
                "transaction_type": self.transaction_type,
                "current_balance": self.current_balance,
                "timestamp": self.timestamp,
            }


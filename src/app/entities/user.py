from typing import Tuple
from ..errors.entity_errors import ParamNotValidated
from ..enums.item_type_enum import ItemTypeEnum

class User:
    name: str
    agency: str
    account: str
    current_balance: float

    def __init__(self, name: str = None, agency: str = None, account: str = None, current_balance: float = None):
        validation_name = self.validate_name(name)
        if validation_name[0] is False:
            raise ParamNotValidated("name", validation_name[1])
        self.name = name

        validation_agency = self.validate_agency(agency)
        if validation_agency[0] is False:
            raise ParamNotValidated("agency", validation_agency[1])
        self.agency = agency

        validation_account = self.validate_account(account)
        if validation_account[0] is False:
            raise ParamNotValidated("account", validation_account[1])
        self.account = account

        validation_current_balance = self.validate_current_balance(current_balance)
        if validation_current_balance[0] is False:
            raise ParamNotValidated("current balance", validation_current_balance[1])
        self.current_balance = current_balance
        
    @staticmethod
    def validate_name(name: str) -> Tuple[bool, str]:
        if name is None:
            return (False, "Name is required")
        if type(name) != str:
            return (False, "Name must be a str")
        if len(name) < 3:
            return (False, "Name must be at least 3 characters long")
        return (True, "")
        
    @staticmethod
    def validate_agency(agency: str) -> Tuple[bool, str]:
        if str is None:
            return (False, "Agency is required")
        if type(agency) != str:
            return (False, "Agency must be a str")
        if len(agency) != 4:
            return (False, "Agency must be a four digit number")
        return (True, "")
    
    @staticmethod
    def validate_account(account: str) -> Tuple[bool, str]:
        if account is None:
            return (False, "Account is required")
        if type(account) != str:
            return (False, "Account must be a str")
        if len(account) != 7:
            return (False, "Account must have a valid format")
        return (True, "")
    
    @staticmethod
    def validate_current_balance(current_balance: float) -> Tuple[bool, str]:
        if current_balance < 0:
            return (False, "Current balance must be positive")
        if type(current_balance) != float:
            return (False, "Current balance must be a float")
        return (True, "")
from typing import Tuple
from ..errors.entity_errors import ParamNotValidated
from ..enums.item_type_enum import ItemTypeEnum

class User:
    name: str
    agency: str
    account: str
    current_balance: float

def __init__(self, name:str= None, agency: str=None, account: str=None, current_balance: float=None):
    validation_name = self.validate_name(name)
    if validation_name[0] is False:
        raise ParamNotValidated("name", validation_name[1])
    self.name = name

    validation_agency = self.validate_agency(agency)
    if validation_agency[0] is False:
        raise ParamNotValidated("agency", validation_agency[1])
    self.agency = agency

    validation_account = self.validation_account(account)
    if validation_account[0] is False:
        raise ParamNotValidated("account", validation_account[1])
    self.account = account

    validation_current_balance = self.validation_current_balance(current_balance)
    if validation_current_balance[0] is False:
        raise ParamNotValidated("current balance", validation_current_balance[1])
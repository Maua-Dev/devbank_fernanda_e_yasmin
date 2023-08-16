from typing import Tuple
from ..errors.entity_errors import ParamNotValidated
from ..enums.item_type_enum import ItemTypeEnum

class User:
    name: str
    agency: str
    account: str
    current_balance: float

def __init__(self, name:srt= None, agency: str=None, account: str=None, current_balance: float=None):
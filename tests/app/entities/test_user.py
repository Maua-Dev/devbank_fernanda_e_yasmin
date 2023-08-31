
import pytest
from src.app.entities.user import User
from src.app.errors.entity_errors import ParamNotValidated


class Test_User:
    def test_user(self):
        user = User(name = "yasmin bonilha", agency = "4444", account =  "12345-6", current_balance = 1000.0)

        assert user.name == "yasmin bonilha"
        assert user.agency == "4444"
        assert user.account == "12345-6"
        assert user.current_balance == 1000.0
    
    def test_name_wrong(self):
        with pytest.raises(ParamNotValidated):
            user = User(name = 0, agency = "4444", account =  "12345-6", current_balance = 67)
    
    def test_agency_wrong(self):
        with pytest.raises(ParamNotValidated):
            user = User(name = "yasmin bonilha", agency = "90000", account =  "12345-6", current_balance = 1000.0)
    
    def test_account_wrong(self):
        with pytest.raises(ParamNotValidated):
            user = User(name = "yasmin bonilha", agency = "77777777777777", account =  "12345-6", current_balance= 1000.0)
    
    def test_current_balance_wrong(self):
        with pytest.raises(ParamNotValidated):
            user = User(name = "yasmin bonilha", agency = "4444", account =  "12345-6", current_balance = 67)
    
        
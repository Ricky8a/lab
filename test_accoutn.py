import pytest
from account import Account

class Test:
    def setup_method(self):
        self.a1 = Account('John')

    def teardown_method(self):
        del self.a1

    def test_init(self):
        assert self.a1.get_name() == 'John'
        assert self.a1.get_balance() == 0.0

    def test_deposit(self):
        # Test with negative amount
        assert self.a1.deposit(-100) == False
        assert self.a1.get_balance() == 0.0

        # Test with zero amount
        assert self.a1.deposit(0) == False
        assert self.a1.get_balance() == 0.0

        # Test with positive amount
        assert self.a1.deposit(500) == True
        assert self.a1.get_balance() == 500.0

    def test_withdraw(self):
        # Test with negative amount
        assert self.a1.withdraw(-100) == False
        assert self.a1.get_balance() == 0.0

        # Test with zero amount
        assert self.a1.withdraw(0) == False
        assert self.a1.get_balance() == 0.0

        # Test with amount greater than balance
        assert self.a1.withdraw(1000) == False
        assert self.a1.get_balance() == 0.0

        # Test with valid withdrawal
        assert self.a1.deposit(500) == True
        assert self.a1.get_balance() == 500.0
        assert self.a1.withdraw(200) == True
        assert self.a1.get_balance() == 300.0

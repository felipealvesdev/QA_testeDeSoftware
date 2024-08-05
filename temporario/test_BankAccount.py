import pytest 
from BankAccount import BankAccount

@pytest.fixture
def account():
    return BankAccount("felipe", 0)
#Aqui a classe foi instanciada
#O valor default da conta é dez

def test_deposit(account):
    account.deposit(100)
    assert account.getUserBalance() == 100

def test_depositNegativeValue(account):
    assert account.deposit(-100) == "Please, deposit only valid values"
    
def test_withdrawal(account):
    account.deposit(1000)
    account.withdrawal(250)
    assert account.getUserBalance() == 750

def test_withdrawalInsufficientBalance(account):
    account.deposit(100)
    assert account.withdrawal(250) == "Insufficient balance for this transaction"
    
def test_getUserBalance(account):
    assert account.getUserBalance() == 0

def test_getUserName(account):
    assert account.getUserName() == "felipe"

def test_multipleOperations(account):
    account.deposit(1410)
    assert account.getUserBalance() == 1410
    account.withdrawal(25)
    assert account.getUserBalance() == 1385
    assert account.getUserName() == "felipe"

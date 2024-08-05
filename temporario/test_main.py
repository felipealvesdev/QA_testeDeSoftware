import pytest 
from main import Calculadora

@pytest.fixture
def calc():
    return Calculadora()

def test_add(calc):
    assert calc.somar(10,5) == 15

def test_subtrair(calc):
    assert calc.subtrair(10,5) == 5
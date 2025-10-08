import pytest
from simplecalc.calculator import Calculator

calc = Calculator()

def test_basic_operations():
    assert calc.calculate("5 * 3") == "15.00"
    assert calc.calculate("5 - 3") == "2.00"

def test_percent():
    assert calc.calculate("200 * 12%") == "24.00"

def test_modulus():
    assert calc.calculate("7 %% 3") == "1.00"

def test_invalid_input():
    with pytest.raises(Exception):
        calc.calculate("hello world")

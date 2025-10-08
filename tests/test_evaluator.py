from decimal import Decimal
import pytest
from simplecalc.evaluator import Evaluator, EvalError

ev = Evaluator()

def test_addition():
    assert ev.eval("2 + 3") == Decimal("5")

def test_modulus():
    assert ev.eval("7 % 3") == Decimal("1")

def test_invalid_expression():
    with pytest.raises(EvalError):
        ev.eval("2 + (3")  # 괄호 오류

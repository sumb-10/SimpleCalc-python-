from decimal import Decimal
from simplecalc.formatter import Formatter

fmt = Formatter()

def test_format_two_decimal():
    assert fmt.format(Decimal("3.14159")) == "3.14"

def test_format_four_decimal():
    assert fmt.format(Decimal("0.009876")) == "0.0099"

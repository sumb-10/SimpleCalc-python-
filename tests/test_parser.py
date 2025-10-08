import pytest
from simplecalc.parser import Parser, ParseError

parser = Parser()

def test_parser_valid_basic():
    assert parser.parse("2 + 3") == "2 + 3"

def test_parser_percent_and_modulus():
    # 12% -> (12*0.01)
    assert parser.parse("200 * 12%") == "200 * (12*0.01)"
    # %% -> %
    assert parser.parse("7 %% 3") == "7 % 3"

def test_parser_invalid_characters():
    with pytest.raises(ParseError):
        parser.parse("import os")  # 허용되지 않은 문자

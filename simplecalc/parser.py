import re
from decimal import Decimal

class ParseError(Exception): pass

class Parser:
    allowed = re.compile(r'^[0-9+\-*/().% ]+$')

    def parse(self, expr: str) -> str:
        if not self.allowed.match(expr):
            raise ParseError("Invalid characters detected")

        expr = expr.strip()

        # 1️⃣ %% → % (Python 나머지 연산자)
        expr = expr.replace("%%", "%")

        # 2️⃣ 단독 % (퍼센트) → *0.01 변환
        expr = re.sub(r'(\d+)%', r'(\1*0.01)', expr)

        return expr

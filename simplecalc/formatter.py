from decimal import Decimal, ROUND_HALF_UP

class Formatter:
    def format(self, x: Decimal) -> str:
        # 기본 2자리, 필요 시 최대 4자리 반올림
        q = Decimal('0.0001') if abs(x) < Decimal('0.01') else Decimal('0.01')
        return str(x.quantize(q, rounding=ROUND_HALF_UP))

    # (선택) 하위호환: 기존 format_eval을 호출해도 동작하도록 유지
    def format_eval(self, result):
        # result가 (Decimal, bool) 형태라도 첫 요소만 사용
        if isinstance(result, tuple) and len(result) >= 1:
            return self.format(result[0])
        return self.format(Decimal(str(result)))

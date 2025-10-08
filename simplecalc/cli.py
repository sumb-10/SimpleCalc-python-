# simplecalc/cli.py
from simplecalc.calculator import Calculator
from simplecalc.parser import ParseError
from simplecalc.evaluator import EvalError

class _Style:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    FG = type("FG", (), {
        "GREEN": "\033[32m",
        "CYAN": "\033[36m",
        "YELLOW": "\033[33m",
        "RED": "\033[31m",
        "MAGENTA": "\033[35m",
        "GRAY": "\033[90m",
        "WHITE": "\033[97m",
    })()

def _banner():
    s = _Style
    print(f"{s.FG.CYAN}{s.BOLD}┌───────────────────────────────────────────┐{s.RESET}")
    print(f"{s.FG.CYAN}{s.BOLD}│               SimpleCalc v1               │{s.RESET}")
    print(f"{s.FG.CYAN}{s.BOLD}└───────────────────────────────────────────┘{s.RESET}")
    print(f"{s.FG.GRAY}명령: {s.FG.WHITE}help{ s.FG.GRAY }, {s.FG.WHITE}history{s.FG.GRAY}, {s.FG.WHITE}clear{s.FG.GRAY}, {s.FG.WHITE}exit{s.RESET}")
    print(f"{s.FG.GRAY}퍼센트: {s.FG.WHITE}200*12% → 24.00{s.FG.GRAY} / 나머지: {s.FG.WHITE}7 %% 3 → 1.00{s.RESET}")
    print(f"{s.FG.GRAY}표시 규칙: 기본 2자리, 필요 시 최대 4자리 반올림{s.RESET}")
    print()

def _help():
    s = _Style
    print(f"{s.FG.MAGENTA}{s.BOLD}[Help]{s.RESET}")
    print(f"  • 산술식 입력: 예) 2+3, 5*3, 200*12% , 7 %% 3")
    print(f"  • {s.FG.WHITE}history{s.RESET}: 최근 5개 계산 내역 보기")
    print(f"  • {s.FG.WHITE}clear{s.RESET}: 화면 지우기")
    print(f"  • {s.FG.WHITE}exit{s.RESET}: 종료")

def _print_history(items):
    s = _Style
    if not items:
        print(f"{s.FG.GRAY}이전 계산 내역이 없습니다.{s.RESET}")
        return
    # 간단한 표 형태로 출력
    print(f"{s.DIM}{'No':>2}  {'Expression':<24}  {'Result':>12}  {'When':<19}{s.RESET}")
    print(f"{s.FG.GRAY}{'-'*64}{s.RESET}")
    for i, h in enumerate(items, 1):
        ts = h.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        expr = (h.expression[:22] + "…") if len(h.expression) > 23 else h.expression
        print(f"{i:>2}  {expr:<24}  {h.result:>12}  {ts:<19}")

class CLI:
    def __init__(self):
        self.calc = Calculator()

    def run(self):
        _banner()
        while True:
            try:
                expr = input(f"{_Style.FG.GREEN}› {_Style.RESET}").strip()
            except (EOFError, KeyboardInterrupt):
                print()  # 줄바꿈
                break

            if not expr:
                continue
            if expr.lower() in ("exit", "quit"):
                break
            if expr.lower() in ("help", "?"):
                _help()
                continue
            if expr.lower() == "clear":
                # ANSI clear
                print("\033[2J\033[H", end="")
                _banner()
                continue
            if expr.lower() == "history":
                _print_history(self.calc.history.list())
                continue

            # 계산 수행
            try:
                result = self.calc.calculate(expr)
                print(f"{_Style.FG.YELLOW}{_Style.BOLD}= {result}{_Style.RESET}")
            except (ParseError, EvalError):
                print(f"{_Style.FG.RED}Error: 잘못된 입력입니다.{_Style.RESET}")
            except Exception:
                # 예기치 못한 오류는 메시지를 통일하되, 프로그램은 계속
                print(f"{_Style.FG.RED}Error: 처리 중 문제가 발생했습니다.{_Style.RESET}")

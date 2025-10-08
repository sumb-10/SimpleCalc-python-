from .parser import Parser
from .evaluator import Evaluator
from .formatter import Formatter
from .history import HistoryManager, HistoryItem

class Calculator:
    def __init__(self):
        self.parser = Parser()
        self.evaluator = Evaluator()
        self.formatter = Formatter()
        self.history = HistoryManager()

    def calculate(self, expr: str) -> str:
        parsed = self.parser.parse(expr)
        value = self.evaluator.eval(parsed)
        result = self.formatter.format(value)
        self.history.add(HistoryItem(expr, result))
        return result
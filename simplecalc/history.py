from datetime import datetime

class HistoryItem:
    def __init__(self, expression: str, result: str):
        self.expression = expression
        self.result = result
        self.timestamp = datetime.now()

class HistoryManager:
    def __init__(self, max_size: int = 5):
        self.max_size = max_size
        self.items = []

    def add(self, item: HistoryItem):
        self.items.insert(0, item)
        if len(self.items) > self.max_size:
            self.items.pop()

    def list(self, limit: int = 5):
        return self.items[:limit]
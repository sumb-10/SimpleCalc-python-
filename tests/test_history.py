from simplecalc.history import HistoryManager, HistoryItem

def test_add_and_list():
    hm = HistoryManager()
    hm.add(HistoryItem("1+2", "3"))
    hm.add(HistoryItem("2+3", "5"))
    items = hm.list()
    assert len(items) == 2
    assert items[0].result == "5"
    assert items[1].expression == "1+2"

def test_limit_max_size():
    hm = HistoryManager(max_size=5)
    for i in range(6):
        hm.add(HistoryItem(f"{i}", str(i)))
    items = hm.list()
    assert len(items) == 5
    assert items[0].result == "5"
    assert items[-1].result == "1"  # 첫 번째 기록은 삭제됨

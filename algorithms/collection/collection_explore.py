"""
This is an exploration of the collection library, problems I've solved with them, and 

"""

from collections import *
from typing import List

# Collections Counter & Default Dict.
class Leetcode1418: # Display Table of Food Orders in a Restaurant
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        result = []
        tables = defaultdict(Counter)
        full_menu = set()
        for _,table,order in orders:
            full_menu.add(order)
            tables[int(table)][order] += 1
        full_menu = ["Table"] + list(sorted(full_menu))
        result.append(full_menu)
        for table, cnt in sorted(tables.items()):
            tablerow = [str(table)]
            for menu_item in full_menu[1:]:
                tablerow.append(str(cnt[menu_item]))
            result.append(tablerow)
        return result

# Collections counter
class Leetcode2363: # Merge Similar Items
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        c = Counter()
        for v, w in items1 + items2:
            c[v] += w
        return sorted(c.items())

# Collections deque
class Leetcode359: # Logging Rate Limiter
    def __init__(self):
        self.timestamp_message = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.timestamp_message:
            if timestamp >= self.timestamp_message[message]:
                self.timestamp_message[message] = timestamp + 10
                return True
            else:
                return False
        else:
            self.timestamp_message[message] = timestamp + 10
            return True


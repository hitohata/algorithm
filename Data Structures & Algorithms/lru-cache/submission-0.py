from collections import deque, defaultdict

class LRUCache:

    def __init__(self, capacity: int):
        self.q = deque()
        self.capacity = capacity
        self.dic = defaultdict()

    def get(self, key: int) -> int:
        return self.dic[key] if key in self.dic else -1
        

    def put(self, key: int, value: int) -> None:
        self.dic[key] = value
        self.q.append(key)
        if len(self.dic) > self.capacity:
            oldest = self.q.popleft()
            del self.dic[oldest]
        

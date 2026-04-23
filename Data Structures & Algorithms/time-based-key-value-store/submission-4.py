class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.mp[key]
        recent = ""
        
        L, R = 0, len(values) - 1
        while L <= R:
            mid = (L + R) // 2
            if values[mid][0] <= timestamp:
                recent = values[mid][1]
                L = mid + 1
            else:
                R = mid - 1
        return recent
        
        

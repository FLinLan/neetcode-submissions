class TimeMap:

    def __init__(self):
        self.time = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        time_values = self.time[key]
        
        L, R = 0, len(time_values) - 1
        recent = ""
        while L <= R:
            mid = (L + R) // 2
            if time_values[mid][0] <= timestamp:
                recent = time_values[mid][1]
                L = mid + 1
            else:
                R = mid - 1
        
        return recent

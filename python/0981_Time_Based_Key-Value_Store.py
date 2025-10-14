class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        low, high = 0, len(self.time_map[key])
        res = ""

        while low < high:
            mid = low + (high - low) // 2

            if self.time_map[key][mid][1] <= timestamp:
                res = self.time_map[key][mid][0]
                low = mid + 1
            else:
                high = mid

        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
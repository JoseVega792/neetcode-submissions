class TimeMap:

    def __init__(self):
        self.contains = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.contains:
            self.contains[key] = []
        self.contains[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res, val = "", self.contains.get(key,[])
        l, r = 0, len(val) - 1
        while l <= r:
            mid = (l + r) // 2
            if val[mid][0] <= timestamp:
                res = val[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res
        
        

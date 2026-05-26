class Status:

    def __init__(self):
        self.timeStamp = []
        self.emotions = []

class TimeMap:

    def __init__(self):
        self.Map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.Map:
            self.Map[key] = Status()

        self.Map[key].timeStamp.append(timestamp) 
        self.Map[key].emotions.append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.Map:
            return ""

        stat = self.Map[key]

        l, r = 0, len(stat.timeStamp) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2

            if stat.timeStamp[mid] <= timestamp:
                res = stat.emotions[mid]
                l = mid + 1
            else:
                r = mid - 1
        return res

        

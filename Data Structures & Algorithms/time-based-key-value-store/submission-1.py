class TimeMap:

    def __init__(self):
        self.timemap = {}
        self.timestamp_prev = 0

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.timemap.get(key) != None:
            if self.timemap[key].get(timestamp) != None:
                self.timemap[key][timestamp].append(value)
            else:
                self.timemap[key][timestamp] = [value]
        else:
            self.timemap[key] = {timestamp:[value]}

        # self.timestamp_prev = timestamp

    def get(self, key: str, timestamp: int) -> str:
        if self.timemap.get(key) != None:
            if self.timemap[key].get(timestamp) != None:
                return self.timemap[key][timestamp][-1]
            else:
                self.timestamp_prev = timestamp
                while self.timestamp_prev != 0:
                    if self.timemap[key].get(self.timestamp_prev - 1) != None:
                        return self.timemap[key][self.timestamp_prev - 1][-1]
                    self.timestamp_prev -= 1
                else:
                    return ""
        else:
            return ""


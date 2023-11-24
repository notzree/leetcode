from collections import defaultdict

class TimeMap:

    def __init__(self):
        #Hash map with array, binary search the array
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        #Since it is strictly increasing, add to end
        self.data[key].append((timestamp, value))
        

    def get(self, key, timestamp):
        arr = self.data[key]
        n = len(arr)
        left = 0
        right = n
        
        while left < right:
            mid = (left + right)// 2
            if arr[mid][0] <= timestamp:
                left = mid + 1
            elif arr[mid][0] > timestamp:
                right = mid
        
        return "" if right == 0 else arr[right - 1][1]

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
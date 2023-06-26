class UndergroundSystem:

    def __init__(self):
        #Dict of tuples
        self.checkMap = {}
        self.routeTime = defaultdict(int)
        self.routeCount = defaultdict(int)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkMap[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        firstEntry = self.checkMap.pop(id)
        firstTime = firstEntry[1]
        firstName = firstEntry[0]

        dt = t-firstTime
        #dt represents the time it took to travel there.
        #popping keeps checkMap small
        
        self.routeTime[firstName+","+stationName] = self.routeTime.get(firstName+","+stationName,0) +dt
        self.routeCount[firstName+","+stationName] = self.routeCount.get(firstName+","+stationName,0)+1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.routeTime[startStation+","+endStation] / self.routeCount[startStation+","+endStation]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
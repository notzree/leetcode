from heapq import heapify, heappush, heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i,s in enumerate(stones):
            stones[i] = -s
        heapify(stones)
        #heapify gives min-heap rather than max-heap
        while stones:
            stone1 = -heappop(stones)
            if not stones:
                return stone1 #Last stone
            stone2 = -heappop(stones)
            if stone1>stone2:
                heappush(stones, stone2-stone1)
        return 0


        


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minEatingSpeed = 1
        maxEatingSpeed = max(piles)
        result = maxEatingSpeed

        while (minEatingSpeed <= maxEatingSpeed):
            currEatingSpeed = (minEatingSpeed+maxEatingSpeed)//2
            hours = 0
            for b in piles:
                hours+= math.ceil(b/currEatingSpeed)
            if hours > h:
                minEatingSpeed = currEatingSpeed+1
            elif hours<=h:
                result = min(result, currEatingSpeed)
                maxEatingSpeed = currEatingSpeed-1
        return minEatingSpeed




        
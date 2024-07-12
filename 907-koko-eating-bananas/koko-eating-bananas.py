class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat(speed: int) -> bool:
            hours = 0
            for p in piles:
                hours += -(-p//speed)
            return hours <= h
        min_eating_speed = 1
        # her maximum eating speed is the max num of banans
        max_eating_speed = max(piles)
        result = max_eating_speed
        while min_eating_speed <max_eating_speed:
            current_speed = (min_eating_speed+max_eating_speed)//2
            if eat(current_speed):
                result = min(result, current_speed)
                #current speed is less than or equal to given speed
                #Can go slower
                max_eating_speed = current_speed
            else:
                min_eating_speed = current_speed+1
        return result






        
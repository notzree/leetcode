class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat(k: int)-> int:
            res = 0
            for b in piles:
                res += math.ceil(b/k)
            return res
        low, high = 1, max(piles)
        res = high
        while low<=high:
            mid = (low+high)//2
            time_taken = eat(mid)
            if time_taken <= h:
                res = min(res, mid)
                #Finished in time. Try eating slower!
                high = mid-1
            else:
                #DNF, eat faster!
                low = mid+1
        return res

            

        






        
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        num_passes = n-1
        remainder = time % num_passes
        rp = (time - remainder)/num_passes
        if rp % 2 == 0:
            f = True
        else:
            f = False
        if remainder ==0:
            if f:
                return 1
            else:
                return n
        if f:
            return 1+remainder
        else:
            return n-remainder
        
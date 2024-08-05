class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        prev_two = 1
        for i in range(n-1):
            prev, prev_two = prev+prev_two, prev
        return prev


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = -99999
        curr_sum = 0

        for i in nums:
            curr_sum = max(curr_sum + i, i)
            best = max(best, curr_sum)
        return best
            
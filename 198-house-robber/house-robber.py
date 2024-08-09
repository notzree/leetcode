class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        prev_one, prev_two = 0, 0
        for i in range(len(nums)):
            prev_one,prev_two = max(prev_two + nums[i], prev_one), prev_one
        return max(prev_one, prev_two)
        


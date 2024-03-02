class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums.sort(key = lambda x : abs(x))
        return map(lambda x: x*x, nums)

        
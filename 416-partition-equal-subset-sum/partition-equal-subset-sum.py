class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_length = len(nums)
        dp = {}  # Use a tuple of (index, current_sum) as keys
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2

        def dfs(i, curr_sum):
            if (i, curr_sum) in dp:  # Check if the state has been computed before
                return dp[(i, curr_sum)]
            if i >= nums_length or curr_sum > target:
                return False
            if curr_sum == target:
                return True
            # Try including the current number
            if dfs(i + 1, curr_sum + nums[i]):
                dp[(i, curr_sum)] = True
                return True
            # Try skipping the current number
            if dfs(i + 1, curr_sum):
                dp[(i, curr_sum)] = True
                return True
            dp[(i, curr_sum)] = False  # Memorize the result
            return False

        return dfs(0, 0)

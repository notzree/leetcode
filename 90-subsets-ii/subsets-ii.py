class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        subset = []
        def dfs(i: int):
            if i == len(nums):
                result.append(subset[:])
                return
            # All subsets that contain nums[i]
            subset.append(nums[i])
            dfs(i+1)
            # All subsets that do not contain nums[i]
            # We need to sort it so that duplicates will be beside each other
            subset.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            dfs(i+1)
        dfs(0)
        return result
            




        
        
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_length = len(nums)
        dp = {}
        total = sum(nums)
        if total%2 !=0:
            return False
        target = total//2
        def dfs(i, curr_sum):
            if i>=nums_length or curr_sum >target:
                return False
            if (i, curr_sum) in dp:  
                return dp[(i, curr_sum)]
            if curr_sum == target: 
                return True
            for j in range(i, nums_length):
                if (j,curr_sum) in dp and dp[(j,curr_sum)] == False:
                    continue
                if dfs(j+1, curr_sum+nums[j]):
                    return True
                else:
                    dp[(j,curr_sum)] = False
            return False
        return dfs(0,0)



            

        
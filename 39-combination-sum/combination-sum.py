class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(combination,i, current_sum):
            if current_sum ==target:
                res.append(combination[:])
                return
            if current_sum > target or i>= len(candidates):
                return
            
            combination.append(candidates[i])
            dfs(combination,i,current_sum+candidates[i])
            combination.pop()
            dfs(combination, i+1, current_sum)

        dfs([],0,0)
        return res
            


        
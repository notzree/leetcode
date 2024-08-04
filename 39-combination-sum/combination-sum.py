class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Basically, for each candidate, you can either choose to take or skip.
        # We simply do this
        result = []
        def dfs(combination: List[int], index: int, s: int):
            if s == target:
                result.append(combination[:])
                return
            if index >=len(candidates) or s >target:
                return
            # Take, this recursive branch represents all the combinations comtaining candidates[index]
            combination.append(candidates[index])
            dfs(combination, index, s+candidates[index]) # Index is the same becuase you can take again
            
            # skip
            combination.pop()
            dfs(combination, index+1,s)
            return
        dfs([],0, 0)
        return result


        
            


        
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort() #Must sort b/c we need to iterate past duplicates.
        def dfs(i, current_combination, current_total):
            #Base case, if out of possible nums or match found
            if current_total ==target:
                res.append(current_combination[:])
                return
            if i >=len(candidates) or current_total >target:
                return
            
            
            #Case where you all soln containing candidates[i] exist
            current_combination.append(candidates[i])
            dfs(i+1, current_combination, current_total+candidates[i])
            current_combination.pop()
             #Case where candidates[i] does not appear AT ALL
            while (i+1<len(candidates) and candidates[i]==candidates[i+1]):
                i+=1
            dfs(i+1, current_combination, current_total)
            
        dfs(0,[],0)
        return res

            


        
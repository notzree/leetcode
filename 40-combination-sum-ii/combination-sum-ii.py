class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort() #Must sort b/c we need to iterate past duplicates.
        # def dfs(i, current_combination, current_total):
        #     #Base case, if out of possible nums or match found
        #     if current_total ==target:
        #         res.append(current_combination[:])
        #         return
        #     if i >=len(candidates) or current_total >target:
        #         return
        # #Case where you all soln containing candidates[i] exist
        #     current_combination.append(candidates[i])
        #     dfs(i+1, current_combination, current_total+candidates[i])
        #     current_combination.pop()
        #      #Case where candidates[i] does not appear AT ALL
        #     while (i+1<len(candidates) and candidates[i]==candidates[i+1]):
        #         i+=1
        #     dfs(i+1, current_combination, current_total)
            
        # dfs(0,[],0)
        # return res

        ##BEtter solution here:
        def dfs(i, current_combination, current_total):
            #Base case, if out of possible nums or match found
            if current_total ==target:
                res.append(current_combination[:])
                return
            if i >=len(candidates) or current_total > target:
                return
            prev = -1
            for i in range(i,len(candidates)):
                if candidates[i] == prev:
                    continue
                current_combination.append(candidates[i])
                #Choosing to use candidates[i]
                dfs(i+1, current_combination, current_total+candidates[i])
                #Choosing to not use candidates[i] is in the i+1 iteration if this makes sense. To me in the future, the ith iteration uses 'chooses' the ith num to start. The i+1 itr would be equivalent to skipping i because we pop the value. 
                current_combination.pop()
                prev = candidates[i]
        dfs(0,[],0)
        return res
            
                

            


        

            


        
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        if len(nums)<1: return []
        start = str(nums[0])
        for i in range(0,len(nums)):
            if i == len(nums)-1 or nums[i]+1 != nums[i+1]: #nums[i-1] end of interval:
                
                if str(nums[i]) == start: #checking if its the last element
                    output.append(str(nums[i]))
                else:
                    output.append(start + "->" + str(nums[i]))
                    
                
                if i!= len(nums)-1:
                    start = str(nums[i+1])
        return output



                
            

            

            
                
            




class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        m = {}
        k = 0
        for n in nums:
            if n not in m:
                m[n] = 1
                nums[k]=n
                k+=1
        return k





        



       
        
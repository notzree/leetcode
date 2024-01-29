class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        m = {}
        k =0
        for n in nums:
            if n not in m:
                nums[k]= n
                m[n] = 1
                k+=1
        return k



       





        



       
        
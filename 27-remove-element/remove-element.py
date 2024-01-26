class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #First part is just iterating and removing
        #Second part is just returning len(nums) - items removed
        last = 0
        for n in nums:
            if n !=val:
                nums[last] = n
                last+=1
            
        return last





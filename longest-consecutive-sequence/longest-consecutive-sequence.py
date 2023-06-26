class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        best = 0
        if len(nums)<1: return 0
        for i in  nums:
            if i-1 not in numSet:
                length = 0
                while (i+length) in numSet:
                    length +=1
                best = max(best,length)
        return best



    




            



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        nc = {}
        for n in nums:
            if n not in nc or nc[n] <=1:
                nums[k]=n
                k+=1
            nc[n] = nc.get(n,0)+1
        return k



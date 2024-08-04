class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # perms = [[]]
        # if len(nums) ==1:
        #     return [nums[:]]
        # for n in nums:
        #     for i in range(len(perms)):
        #         p = perms.pop(0) # Remove the existing permutation
        #         for j in range(len(p)+1):
        #             p_copy = p.copy()
        #             p_copy.insert(j,n)
        #             perms.append(p_copy)
        # return perms
        if len(nums) ==0:
            return [[]]
        perms = self.permute(nums[1:])
        res = []
        for p in perms:
            for i in range(len(p)+1):
                p_copy = p.copy()
                p_copy.insert(i,nums[0])
                res.append(p_copy)
        return res



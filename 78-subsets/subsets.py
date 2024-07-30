class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.s = set()
        def populate(combination, idx):
            if idx == len(nums):
                self.s.add(tuple(combination))
                return
            populate(combination, idx+1)
            populate(combination + [nums[idx]],idx+1)
        populate([], 0)
        return self.s



                



        
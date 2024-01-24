class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset[:])
                return
            #Decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)

            #Decision to skip nums[i]
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res

        #Me trying the BFS way
        # # u start with [] -> copy and add [n] --> [],[1],[2],[3] repeat.
        # res = [[]]
        # for n in nums:
        #     for i in range(len(res)):
        #         subset = res[i][:]
        #         subset.append(n)
        #         res.append(subset)
        # return res
                



        
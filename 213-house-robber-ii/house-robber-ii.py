class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0], nums[1])
        
        firstmax, secondmax = 0,0
        #Decide to rob 1st, can't rob last
        rob1,rob2 = 0,0
        for n in range(len(nums)-1):
            temp = max(rob1+nums[n], rob2)
            rob1=rob2
            rob2=temp
        firstmax = rob2

        rob1,rob2 = 0,0

        for n in range(1,len(nums)):
            temp = max(rob1+nums[n], rob2)
            rob1=rob2
            rob2=temp
        secondmax = rob2
        return max(firstmax,secondmax)

        
        

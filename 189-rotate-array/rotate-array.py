class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums2 = nums[:] #Make sure to copy it, not reference it
        for i in range(0,len(nums2)):
            j = (i+k)% len(nums2)
            nums[j] = nums2[i]
        

        
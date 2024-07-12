class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(nums: List[int], low, high)->int:
            if low>=high: return -1
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            if nums[mid] <=target:
                return bs(nums,mid+1,high)
            else:
                return bs(nums, low, mid)
        return bs(nums, 0, len(nums))



        
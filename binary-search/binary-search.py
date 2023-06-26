class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def search(nums,target,low,high):
            if low>=high: return -1
            
            mid = (low + high)//2
            if nums[mid] == target:
                return mid
            if (nums[mid]<target):
                return search(nums,target,mid+1,high)
            else:
                return search(nums,target,low,mid)

        return search(nums,target,0,len(nums))



        
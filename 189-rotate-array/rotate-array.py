class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(array, start, end):
            while start<=end:
                array[start], array[end] = array[end], array[start]
                start+=1
                end-=1
            return array
        k = k%len(nums)
        
        nums.reverse()
        reverse(nums,0,k-1)
        reverse(nums,k, len(nums)-1)
        return nums


        


        
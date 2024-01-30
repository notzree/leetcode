class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # def partition(nums, low, high):
        #     pivot = nums[high]
        #     i = low-1
        #     for j in range(low,high):
        #         if nums[j]<=pivot:
        #             i = i+1
        #             #Swap elements in array that are out of place
        #             (nums[i], nums[j]) = (nums[j], nums[i])
        #         #Swap pivot element (array[high]) with the greatest element in this iteration that is less than pivot. (array[i+1])
        #     (nums[i+1], nums[high]) = (nums[high], nums[i+1])
        #     return i+1
        # def quickSort(nums, low, high):
        #     if low<=high: 
        #         pi = partition (nums, low, high)
        #         quickSort(nums, low, pi-1)
        #         quickSort(nums,pi+1, high)

        # quickSort(nums,0,len(nums)-1)
        # return nums

        #Merge sort
            def merge(nums, L,M,R):
                left, right = nums[L:M+1], nums[M+1:R+1]
                i = L
                j,k = 0,0
                while j< len(left) and k < len(right):
                    if left[j] <=right[k]:
                        nums[i] = left[j]
                        j+=1
                    else:
                        nums[i] = right[k]
                        k+=1
                    i+=1
                while j <len(left):
                    nums[i] = left[j]
                    j+=1
                    i+=1
                while k <len(right):
                    nums[i] = right[k]
                    k+=1
                    i+=1

            def mergesort(nums, left, right):
                #Base case, array we are sorting is length 1
                if left == right:
                    return nums
                middle = (left+right)//2
                mergesort(nums, left, middle) #Left-> mid
                mergesort(nums,middle+1,right) #mid+1 -> Right
                #Merge the array (modified inplace)
                merge(nums, left, middle, right)
                return nums
            return mergesort(nums,0, len(nums)-1)


            


                





        
        
class Solution:
    def trap(self, height: List[int]) -> int:
    
        left, right = 0, len(height)-1
        water = 0
        lMax, rMax = height[left],height[right]
        while (left<right):
            if height[left]< height[right]:
                #only consider left side as left is the bounding
                left = left +1
                lMax = max(lMax,height[left])
                
                water += lMax - height[left]
            else:
                right = right -1
                rMax = max(rMax,height[right])
                
                water += rMax-height[right]
        return water

            
        

        
        
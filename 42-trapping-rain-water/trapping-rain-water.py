class Solution:
    def trap(self, height: List[int]) -> int:
    
        left, right = 0, len(height)-1
        water = 0
        lMax, rMax = height[left],height[right]
        while left < right:
            if height[left] < height[right]:
                #Left height is the limiting factor
                left = left + 1
                #Track the greatest height on the lhs.
                lMax = max(lMax, height[left]) 
                # if height[left] > lMax (current block is tallest) we would not add any water
                water += lMax-height[left]
            else:
                right = right - 1 
                #Right becomes the limiting factor (or they are equal, either way same logic)
                rMax = max(rMax, height[right])
                water += rMax - height[right]
        return water
        
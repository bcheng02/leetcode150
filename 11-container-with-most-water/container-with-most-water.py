class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        ptr1 = 0
        ptr2 = len(height) - 1
        
        while (ptr1 < ptr2):
            currArea = (ptr2 - ptr1) * min(height[ptr1], height[ptr2])
            maxArea = max(maxArea, currArea)
            
            if (height[ptr1] < height[ptr2]):
                ptr1 += 1
            else:
                ptr2 -= 1
        
        return maxArea
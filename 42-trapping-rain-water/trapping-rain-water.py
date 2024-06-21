class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        water = 0
        ptr1 = 0
        ptr2 = len(height) - 1
        lmax = height[ptr1]
        rmax = height[ptr2]
        
        while(ptr1 < ptr2):
            if lmax < rmax:
                ptr1 += 1
                lmax = max(lmax, height[ptr1])
                water += lmax - height[ptr1]
            else:
                ptr2 -= 1
                rmax = max(rmax, height[ptr2])
                water += rmax - height[ptr2]
            
        return water
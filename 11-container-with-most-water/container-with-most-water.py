class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lptr, rptr = 0, len(height) - 1
        maxWater = 0

        while(lptr < rptr):
            maxWater = max(maxWater, min(height[lptr], height[rptr]) * (rptr-lptr))
            if (height[lptr] < height[rptr]):
                lptr += 1
            else:
                rptr -= 1

        return maxWater
                
        
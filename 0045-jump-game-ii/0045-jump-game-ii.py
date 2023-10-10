class Solution:
    def jump(self, nums: List[int]) -> int:
        # this is neetcode sol'n. i got stuck bec this is the first time i've seen such a problem
        
        l = r = 0
        result = 0
        
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, nums[i] + i)
            l = r + 1
            r = farthest
            result+=1
        
        return result
            
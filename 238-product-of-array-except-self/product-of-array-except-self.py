class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        ans = []

        for i in range(len(nums)):
            if (i == 0): prefix[i] = nums[i]
            else: prefix[i] = nums[i] * prefix[i - 1]

        for i in range(len(nums) - 1, -1, -1):
            if (i == len(nums) - 1): suffix[i] = nums[i]
            else: suffix[i] = nums[i] * suffix[i + 1]
        
        for i in range(len(nums)):
            if (i == 0):
                ans.append(1 * suffix[i + 1])
            elif (i == len(nums) - 1):
                ans.append(prefix[i - 1] * 1)
            else: 
                ans.append(prefix[i - 1] * suffix[i + 1])

        return ans

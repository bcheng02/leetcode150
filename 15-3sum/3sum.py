class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        
        for i, num in enumerate(nums):
            if (i != 0 and num == nums[i - 1]): continue
            
            l, r = i + 1, len(nums) - 1
            while(l < r):
                amount = num + nums[l] + nums[r]
                if (amount < 0):
                    l += 1
                elif (amount > 0):
                    r -= 1
                else:
                    ans.append([num, nums[l], nums[r]])
                    l += 1
                    while (nums[l] == nums[l - 1] and l < r):
                        l += 1   
        return ans
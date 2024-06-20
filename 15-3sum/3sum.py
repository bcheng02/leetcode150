import math

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        ans = []
        
        for i in range(len(nums)):
            if (i > 0 and nums[i] == nums[i-1]): continue
            
            ptr1 = i + 1
            ptr2 = len(nums) - 1
            while(ptr1 < ptr2):
                sum = nums[ptr1] + nums[ptr2] + nums[i]
                
                if (sum < 0):
                    ptr1 += 1
                elif (sum > 0):
                    ptr2 -= 1
                else:
                    ans.append([nums[i], nums[ptr1], nums[ptr2]])
                    
                    # if ptr1's next value is same, then want to keep going
                    # only need to change ptr1 since ptr2 will be updated with other code
                    ptr1 += 1
                    while (nums[ptr1] == nums[ptr1 - 1] and ptr1 < ptr2):
                        ptr1 += 1
                    
    
        return ans
        
        
        
        
            
        
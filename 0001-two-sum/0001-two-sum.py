class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        
        
        myMap = { nums[i]: i for i in range(length)}
        
        for i in range(length):  
            if ((target - nums[i]) not in myMap or myMap[target - nums[i]] == i):
                continue
            
            print(myMap)
            return [ i , myMap[target - nums[i]] ]
        
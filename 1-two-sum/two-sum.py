class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = i
        
        for i in range(len(nums)):
            currVal = nums[i]
            newTarg = target - currVal
            
            if (newTarg in map) and (map[newTarg] != i):
                return [i, map[newTarg]]
        
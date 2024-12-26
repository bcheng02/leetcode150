class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        map = {}
        
        for num in nums:
            if num not in map:
                map[num] = True
            else: return True
        
        return False
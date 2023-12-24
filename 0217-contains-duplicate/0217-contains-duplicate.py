class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mySet = set(nums)    
        return len(mySet) != len(nums) 
       
    
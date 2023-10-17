class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:   
        mySet = set(nums)
        longest = 0 # for the empty set & keeps a running tally since length itself isn't saved
        
        
        for n in mySet: 
            if (n-1 not in mySet):
                length = 1
                while (n + length) in mySet:
                    length += 1
                longest = max(longest, length)
        return longest 
                
                
                    
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if (len(set(nums)) == 1):
#             return 1
        
#         mySet = set()
#         tally = 0

        
#         for n in nums:
#             mySet.add(n-1)
#             mySet.add(n+1)
               
        
#         for n in nums:
#             if (n in mySet): 
#                 mySet.remove(n)
#                 tally += 1
                
#         return tally
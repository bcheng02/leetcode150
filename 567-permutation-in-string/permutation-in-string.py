class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        # look in window of sizes of len(s1) in s2, check to see if window contains all chars of s1
        
        start = 0
        s1 = sorted(s1)
    
        for end in range(len(s1) - 1, len(s2)):
            if (sorted(s2[start:end+1]) == s1):
                return True
            
            start += 1
            
        
        return False
        
     
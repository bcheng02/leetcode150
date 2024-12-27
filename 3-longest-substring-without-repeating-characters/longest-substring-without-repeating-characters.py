class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        start = 0
        maxLen = 0
        seen = {}
        
        for end, val in enumerate(s):
            if (val in seen):
                while(val in seen):
                    del seen[s[start]] # can't just set to False since val in seen doesn't work
                    start += 1
                seen[val] = True
            else:
                seen[val] = True
                maxLen = max(maxLen, end - start + 1)
            
        return maxLen
        
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
                start = end
                seen.clear()
                while(s[start - 1] != val):
                    # print(s[start-1])
                    seen[s[start-1]] = True
                    start -= 1
                seen[val] = True
            else:
                seen[val] = True
                maxLen = max(maxLen, end - start + 1)
            
        return maxLen
        
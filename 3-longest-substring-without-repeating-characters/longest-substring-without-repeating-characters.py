class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        start = 0
        maxLen = 0
        seen = set()
        
        for end, item in enumerate(s):
            if (item not in seen):
                seen.add(item)
                maxLen = max(maxLen, end-start+1)
            else:
                seen = set()
                seen.add(item)
                
                start = end
                while (s[end] != s[start - 1]):
                    seen.add(s[start - 1])
                    start -= 1
                print(start)
                maxLen = max(maxLen, end-start+1)

        return maxLen
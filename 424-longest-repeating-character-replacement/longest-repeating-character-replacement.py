class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        maxLen = 0
        start = 0
        count = {}
        
        for end, val in enumerate(s):
            count[s[end]] = count.get(s[end], 0) + 1
            if (end-start+1 - max(count.values())) <= k:
                maxLen = max(end-start+1, maxLen)
            else:
                count[s[start]] -= 1
                start += 1

        return maxLen

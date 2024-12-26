class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if (len(s) != len(t)): return False

        sMap, tMap = {}, {}
        for i in range(len(s)):
            sMap[s[i]] = sMap.get(s[i], 0) + 1
            tMap[t[i]] = tMap.get(t[i], 0) + 1

        for char in s:
            if (sMap[char] != tMap.get(char, 0)): return False

        return True
            
        # return sorted(s) == sorted(t)
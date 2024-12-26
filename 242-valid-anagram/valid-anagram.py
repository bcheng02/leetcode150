class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # map = {}
        # for char in s:
        #     if (char not in map):
        #         map[char] = 0
        #     map[char] = map[char] += 1
        
        return sorted(s) == sorted(t)
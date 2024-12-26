class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        newStr = ''.join(c.lower() for c in s if c.isalnum())
        
        lptr = 0
        rptr = len(newStr) - 1
        
        while (lptr < rptr):
            if (newStr[lptr] != newStr[rptr]):
                return False
            lptr += 1
            rptr -= 1
        return True
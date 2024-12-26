class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newStr = ''.join(char.lower() for char in s if char.isalnum())
        
        # newStr = ''
        # for c in s:
        #     if (c.isalnum()):
        #         newStr += c.lower()
        
        lptr = 0
        rptr = len(newStr) - 1
        
        while (lptr < rptr):
            if (newStr[lptr] != newStr[rptr]):
                return False
            lptr += 1
            rptr -= 1
        return True
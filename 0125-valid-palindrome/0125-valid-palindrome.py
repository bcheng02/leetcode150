class Solution:
    def isPalindrome(self, s: str) -> bool:
        # include only letters & numbers w/ regex: isalnum()
        # put in arr = reverse arr
        
        charArr = list(s)
        # print( charArr )
        filtArr = (list(filter(lambda x: x.isalnum(), charArr))) # hm, so filter returns an iterable and we need to convert to list
        print( filtArr )
        print( list(reversed(filtArr)))

        return ''.join(filtArr).lower() == ''.join(list(reversed(filtArr))).lower()
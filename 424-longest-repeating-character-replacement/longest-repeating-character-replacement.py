class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        start = 0
        maxLen = 0
        count = {}
        
        for end in range(len(s)):
            count[s[end]] = 1 + count.get(s[end], 0)
            
            if (end-start+1 - max(count.values()) <= k):
                maxLen = max(maxLen, end-start+1)
                
            else: 
                count[s[start]] -= 1
                start += 1
                maxLen = max(maxLen, end-start+1)
                
        
        
        return maxLen
            
        
        
        # we know that the window will be at least size k and at most size n, since 
            # 0 <= k <= s.length, so k will always be at most the size of the string
            # then we can replace k adjacent chars with the same char
        
        # maxLen = max(maxLen, end-start+1)
        
        
        # problems
            # idk what exactly is going to make it longest repeating. it's not the most frequent and it's not the most consecutive..what's the trick is there even a trick???
                # not most consecutive: c c b d b d b. most consec is c. correct repeating char is b
                # not most frequent: 
            # how can we have a "global picture" (know where things are and where to place the character without there being a trick) unless we have to iterate thru the list a bunch of times??? (up to n^k)
            
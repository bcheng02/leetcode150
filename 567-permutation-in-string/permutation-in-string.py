class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        if len(s1) > len(s2):
            return False
        
        start = 0
        s1Arr = [0] * 26
        s2Arr = [0] * 26
        matches = 0
        
        for i in range(len(s1)):
            s1Arr[ord(s1[i]) - ord('a')] += 1
            s2Arr[ord(s2[i]) - ord('a')] += 1

        for i in range(26):
            if (s1Arr[i] == s2Arr[i]):
                matches += 1
            
        for end in range(len(s1), len(s2)): 
            if matches == 26: return True
            
            # add new, update matches
            index = ord(s2[end]) - ord('a')
            s2Arr[index] += 1
            if (s1Arr[index] == s2Arr[index]): 
                matches += 1
            elif (s1Arr[index] == s2Arr[index] - 1):
                matches -= 1
                
            # remove old, update matches
            index = ord(s2[start]) - ord('a')
            s2Arr[index] -= 1
            if (s1Arr[index] == s2Arr[index]): 
                matches += 1
            elif (s1Arr[index] == s2Arr[index] + 1):
                matches -= 1
                
            start += 1
        
        return matches == 26
        
        
        # make 2 arrays that represent letters of alphabet and their counts
        # make a matches variable that compares how many letters match
        # loop thru s2 in correct window sizes and update the pointers, arrays, and matches variable
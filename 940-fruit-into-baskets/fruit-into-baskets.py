class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        maxFruit = 0
        start = 0
        seen = set()
        
        for end, fruit in enumerate(fruits):
            if (len(seen) < 2 and fruit not in seen):
                seen.add(fruit)
                maxFruit = max(maxFruit, end-start+1) # it's not maxFruit += 1 because the answer is going to be the window size. and after you resize the window, the window may be smaller than your previous max. however the window may eventually grow larger than the previous max but you aren't even checking that.
            elif (fruit in seen):
                maxFruit = max(maxFruit, end-start+1) 
            else:
                seen = set()
                seen.add(fruits[end - 1])
                seen.add(fruit)
                
                start = end - 1
                
                while (fruits[start] == fruits [start - 1]):
                    start -= 1
                
                maxFruit = max(maxFruit, end-start+1)
                
                
            
        return maxFruit
            
            
        
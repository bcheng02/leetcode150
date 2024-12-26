class Solution(object):
    def isPalindrome(self, s):
        filtered = list(filter(lambda x: x.isalnum(), s))
        filtered_lower = list(map(lambda x: x.lower(), filtered))
        
        if filtered_lower == []: return True
        
        # 2 pointers 
        ptr1 = 0
        ptr2 = len(filtered_lower) - 1
        
        while(ptr1 < ptr2):
            if filtered_lower[ptr1] != filtered_lower[ptr2]:
                return False
            ptr1 += 1
            ptr2 -= 1
            
        return True
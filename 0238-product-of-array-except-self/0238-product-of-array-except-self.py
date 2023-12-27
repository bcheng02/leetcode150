class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # pre-fix, post-fix, then combine. that's O(3n) = O(n)
        
        # prefix
        prefix = []
        
        for i, n in enumerate(nums):
            if (i == 0):
                prefix.append(n)
            else:
                prefix.append(n * prefix[i-1])
        
        print(prefix)
              
              
        # postfix
        postfix = []
        
        for i, n in enumerate(reversed(nums)):
            if (i == 0):
                postfix.append(n)
            else:
                postfix.append(n * postfix[i-1])
        
        postfix.reverse()
        print(postfix)
        
        
        # put together
        ans = []
        
        for i, n in enumerate(nums):
            num1 = 1 if i-1 < 0 else prefix[i-1]
            num2 = 1 if i+1 > (len(nums) - 1) else postfix[i+1]
            ans.append(num1 * num2)
            
        
        return ans
            
            
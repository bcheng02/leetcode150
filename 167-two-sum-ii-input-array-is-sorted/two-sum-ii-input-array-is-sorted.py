class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        lptr, rptr = 0, len(numbers) - 1
        
        while(lptr < rptr):
            sum = numbers[lptr] + numbers[rptr]
            
            if (sum > target):
                rptr -= 1
            elif (sum < target):
                lptr += 1
            else:
                return [lptr + 1, rptr + 1]
        
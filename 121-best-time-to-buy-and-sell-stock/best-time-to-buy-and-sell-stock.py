class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxP = 0
        start = 0
        for end in range(len(prices)):
            if prices[end] < prices[start]:
                start = end
            else: 
                maxP = max(maxP, prices[end] - prices[start])
        return maxP
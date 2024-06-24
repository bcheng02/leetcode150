class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        lowest = prices[0]
        
        for price in prices:
            if (price < lowest):
                lowest = price
            maxProfit = max(maxProfit, price - lowest)    
            
        
        return maxProfit
        
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        min = prices[0]
        max_profit = 0
        for price in prices:
            if price < min:
                min = price
            elif price - min > max_profit:
                max_profit = price - min
        return max_profit


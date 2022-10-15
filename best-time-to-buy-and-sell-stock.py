class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        i = 0
        while i < len(prices)-1:
            curr = max(prices[i+1:]) - prices[i]
            maxProfit = max(maxProfit, curr)
            i += 1
        return maxProfit

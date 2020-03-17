"""
Procedure:
At each step of the iteration calculate the minimum and the current profit.
The dp table will contain the maximum profit earned at each day, which is
either the profit from the previous day or the current profit

Complexity:
n -> length of prices
Time: O(n)
Space: O(n)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        dp = [0] * (len(prices) + 1)
        minimum = float('inf')
        
        for i, val in enumerate(prices, 1):
            minimum = min(val, minimum)
            profit = val - minimum
            dp[i] = max(dp[i-1], profit)
            
        return dp[-1]
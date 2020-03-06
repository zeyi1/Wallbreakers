"""
Procedure:
Using recursion and memoization.
The idea is to have a currentMinimum for each recursive call, and a dictionary to keep track of the
highest profit that can be made at each day.
The dictionary will be populated by taking the maximum of (currentPrice - currentMin) and (recursive
call to the next day).
Once it reaches the last day, it will populate back the maximumProfit earned in those future days and
compare with what can be earned at the current day, until the first day.

Complexity:
n -> length of input list
Time: O(n)
Space: O(n)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        memo = {}
        minimum = prices[0]
        
        return self.helper(prices, minimum, memo, 1)
        
        
    def helper(self, prices, minimum, memo, index):
        if index == len(prices) - 1:
            return max(0, prices[index] - minimum)
        
        minimum = min(minimum, prices[index])
        
        if index not in memo:
            memo[index] = max(prices[index] - minimum, self.helper(prices, minimum, memo, index + 1))
            
        return memo[index]
            
"""
Procedure:
The sister can get at most (numberOfCandies // 2) candies since the candies must be distributed evenly with her brother.
Use a set to get distinct number of candies, if the number of distinct candies is lower than what the sister can hold,
then she can only get those distinct candies. If there are more distinct candies than what she can hold, she can only
get what she can hold.

Complexity:
n -> number of candies
Time: O(n)
Space: O(n)
"""

class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        if not candies:
            return 0
        
        uniqueCandies = len(set(candies))
        sisterTotalCandies = len(candies) // 2
        
        if uniqueCandies <= sisterTotalCandies:
            return uniqueCandies
        
        else:
            return sisterTotalCandies
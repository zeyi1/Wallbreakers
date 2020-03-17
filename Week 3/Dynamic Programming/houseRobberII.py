"""
Procedure:
Create two dp tables, one that will account for the first house and ignore the last house, 
and one that starts from the second house and account for the last house.
Each index will contain the maximum that can be earned from robbing the current house and the
house before the previous house or just robbing the previous house.

Complexity:
n -> number of houses
Time: O(n)
Space: O(n)
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) < 2:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums)
        
        memo = [0] * len(nums)
        memo2 = memo[:]
        memo[1], memo2[1] = nums[0], nums[1]
        
        for i in range(1, len(nums) - 1):
            memo[i+1] = max(memo[i-1] + nums[i], memo[i])
            memo2[i+1] = max(memo2[i-1] + nums[i+1], memo2[i])

        
        return max(memo[-1], memo2[-1])

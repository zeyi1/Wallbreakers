"""
Procedure:
Same as house robber, in this problem, the first house cannot be robbed together with the last house,
so the result will be the maximum of nums[1:] and nums[:-1], another cache is required so that the 
second call does not use the values already populated by the first call.

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
        
        memo = [-1] * len(nums)
        memo2 = [-1] * len(nums)
        result = max(self.helper(nums[1:], len(nums) - 2, memo), self.helper(nums[:-1], len(nums) - 2, memo2))
        
        return result
        
        
    def helper(self, nums, index, memo):
        
        if index < 0:
            return 0
        
        if memo[index] >= 0:
            return memo[index]
        
        memo[index] = max(self.helper(nums, index - 2, memo) + nums[index], self.helper(nums, index - 1, memo))

        return memo[index]
        
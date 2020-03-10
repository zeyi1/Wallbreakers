"""
Procedure:
Get the total sum of nums and check whether is divisible by 2.
Target value will be half of that sum.
Create a helper function, base case will be when target becomes 0, recurse by subtracting target with
the current number and incrementing the index for the next number. Memoize the targets, and if target
is less than 0, backtrack to previous calls.

Complexity:
n -> length of input list, m -> total of all numbers
Time: O(n * m)
Space: O(n)
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        
        total = sum(nums)
        if total % 2 == 1: 
            return False
            
        target = total // 2   
        maxVal = max(nums)
        
        if maxVal > target:
            return False
        
        return self.helper(nums, target, 0, len(nums), {})  
        
        
    def helper(self, nums, target, index, length, d):
        if target in d:
            return d[target]
        
        if target == 0:
            d[target] = True
            
        else:
            d[target] = False
            if target > 0:
                for i in range(index, length):
                    if self.helper(nums, target - nums[i], i+1, length, d):
                        d[target] = True
                        break
                        
        return d[target]
    

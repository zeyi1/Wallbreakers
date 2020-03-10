"""
Procedure:
The total sum should be divisible by k, and the target is that division.
Create a helper function, that takes k (number of buckets), index, curListSum and a dictionary.
The base case will be when k reaches 1, that means all other 3 buckets were successfully splitted,
so the remaining numbers must add up to target.
Once a bucket equals target, we recurse with default parameters and reduce k.
The dictionary keeps the index as keys, and if that index is used is marked as True, otherwise False
to backtrack.

Complexity:
n -> length of input list
Time: O(2^n)
Space: O(n)
"""

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        
        total = sum(nums)
        
        if total % k != 0:
            return False
        
        target = total // k
        maxVal = max(nums)
        if maxVal > target:
            return False
        
        d = {i: False for i in range(len(nums))}
        
        return self.helper(nums, target, k, 0, 0, d)
    
        
    def helper(self, nums, target, k, index, curListSum, d):
        if k == 1:
            return True
        
        if curListSum == target:
            return self.helper(nums, target, k-1, 0, 0, d)
        
        for i in range(index, len(nums)):
            if not d[i]:
                d[i] = True
                if self.helper(nums, target, k, i+1, curListSum + nums[i], d):
                    return True
                
                d[i] = False      
                
        return False
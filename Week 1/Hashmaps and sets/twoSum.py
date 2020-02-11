"""
Procedure:
Create a dictionary that will contain the numbers we already visited as keys and their respective index as values.
Calculate the difference at each step and if we find this difference in the dictionary return both indices.

Complexity:
n -> length of input list
Time: O(n)
Space: O(n)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        
        for i, num in enumerate(nums):
            diff = target - num
            
            if diff in d:
                return [d[diff], i]
            
            d[num] = i

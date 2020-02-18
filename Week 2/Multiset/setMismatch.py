"""
Procedure:
Use two sets, one set will contain numbers from 1 to n, while the other will find the duplicate number.
Use set difference, to get the missing number.

Complexity:
n -> length of input list
Time: O(n)
Space: O(n)
"""

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        missing, seen = set(), set()
        duplicate = 0
        
        for index, num in enumerate(nums, 1):
            missing.add(index)
            if num in seen:
                duplicate = num
                
            seen.add(num)
            
        missing = missing - seen
        
        return [duplicate] + list(missing)
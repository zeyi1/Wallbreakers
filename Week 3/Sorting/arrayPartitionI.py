"""
Procedure:
Since it wants the maximum sum of the minimum of pairs, we need to exhaust all lower values by
pairing the 2 lowest each time. So sort in ascending order and get the even index numbers.

Complexity:
n -> length of input list
Time: O(nlogn)
Space: O(n)
"""

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        
        maxMinSum = 0
        
        for num in sortedNums[::2]:
            maxMinSum += num
            
        return maxMinSum
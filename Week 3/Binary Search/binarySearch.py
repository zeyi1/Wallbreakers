"""
Procedure:
Two pointers left and right to point to the beginning and end of array.
Mid will be left + (right-left)//2 to prevent overflow.
Condition must be left <= right so that mid can reach the rightmost index.

Complexity:
n -> length of input list
Time: O(logn)
Space: O(1)
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left)//2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                left = mid + 1
                
            else:
                right = mid - 1
                
        return -1
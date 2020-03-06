"""
Procedure:
If k is greater than the size of the list, subtract it by the size of the list until its smaller because it would end up in
the same rotated numbers. Store in a queue the numbers up to index (size of list - k).
The new index of elements will be curIndex + (size of list - k), if this new index is greater than size of list, pop the 
elements from the queue as this number corresponds in this index.

Complexity:
n -> length of input list
Time: O(n)
Space: O(n - k)
"""

from collections import deque

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) < 2:
            return
        
        while k > len(nums):
            k -= len(nums)
            
        queue = deque()
        diff = len(nums) - k
        
        for i in range(diff):
            queue.append(nums[i])
            
        for i in range(len(nums)):
            newIndex = i + diff
            if newIndex >= len(nums):
                nums[i] = queue.popleft()
                
            else:
                nums[i] = nums[newIndex]
"""
Procedure:
Perform binary search, if the value at mid is greater than the previous and next elements, we found the peak.
If the value at mid is less than the previous one, the peak is on the left side, otherwise on the right side.

Complexity:
n -> length of input array
Time: O(logn)
Space: O(1)
"""

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        left, right = 0, len(A) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            if mid > 0 and mid < len(A) - 1:
                if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
                    return mid
                
                elif A[mid] < A[mid-1]:
                    right = mid - 1
                
                else:
                    left = mid + 1
                    
        return -1
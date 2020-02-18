"""
Procedure:
Convert both lists to sets, and calculate the intersection using bitwise and operator.

Complexity:
n -> length of nums1, m -> length of nums2
Time: O(max(n, m))
Space: O(max(n, m))
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1, set2 = set(nums1), set(nums2)
        
        return set1 & set2
"""
Procedure:
Use two pointers (left, right) to point to the beginning and the end of the list.
Swap the values between them, increment and decrement the pointers respectively until left >= right.

Complexity:
n -> length of s
Time: O(n / 2) -> O(n)
Space: O(1)
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s or len(s) == 1:
            return s
        
        left, right = 0, len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
            
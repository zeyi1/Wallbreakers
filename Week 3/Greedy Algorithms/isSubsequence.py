"""
Procedure:
Use a pointer for s and an auto increment pointer for t.
If the character at s matches the character at t, increment s pointer.
At the end, if s pointer is equal to length of s, then we found the subsequence.

Complexity:
n -> length of t
Time: O(n)
Space: O(1)
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        if not t:
            return False
        
        sLen, tLen = len(s), len(t)
        left, right = 0, 0
        
        while left < sLen and right < tLen:     
            if s[left] == t[right]:
                left += 1
            
            right += 1
            
        return left == sLen
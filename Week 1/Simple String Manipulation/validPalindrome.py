"""
Procedure:
Use two pointers (left, right) to point to the beginning and end of the string.
Loop until left >= right, at each iteration keep moving the pointers until they reach
an alphanumeric character and making sure left < right holds true.
If the character at left does not match the character at right, then it is not a palindrome.

Complexity:
n -> length of input string
Time: O(n)
Space: O(1)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s or len(s) == 1:
            return True
        
        left, right = 0, len(s) - 1
        
        while left < right:
            while not s[left].isalnum() and left < right:
                left += 1
                
            while not s[right].isalnum() and left < right:
                right -= 1
                
            if s[left].lower() != s[right].lower():
                return False
            
            left, right = left + 1, right - 1
            
        return True
"""
Procedure:
In Python strings are immutable, so is better to convert the string into a list, perform the swapping and then convert back into string.
Use two pointers to get the position of the outer vowels, and work our way in.

Complexity:
n -> length of input string
Time: O(n)
Space: O(n)
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        if not s:
            return ""
        
        vowels = set('aeiou')
        s = list(s)
        left, right = 0, len(s) - 1
        
        while left < right:
            while s[left].lower() not in vowels and left < right:
                left += 1
                
            while s[right].lower() not in vowels and left < right:
                right -= 1
                
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
            
        return ''.join(s)
        
"""
Procedure:
Split the string by whitespace.
Reverse each word and concatenate them with whitespaces.

Complexity:
n -> length of input string
Time: O(n)
Space: O(n)
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        
        splitS = s.split(' ')
        
        return ' '.join(word[::-1] for word in splitS)
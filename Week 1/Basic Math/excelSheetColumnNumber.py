"""
Procedure:
Create a dictionary containing the alphabet and its respective value.

For each position, we have 26 choices (A-Z).
Length one can be represented as 26^0 * Char.value
Length two's values starts from max of length one's value (26). Each letter at position 0 can have 26 combinations and we can choose 26 letters.
Length two will be 26^1 * Char.value + max of previous length
It can be generalized to -> (26^(length-1) * Char.value) + (26^(length-2) * Char.value) + ... + (26^0 * Char.value)

Complexity:
n -> length of input string
Time: O(26*n) -> O(n)
Space: O(26) -> O(1)
"""

import string

class Solution:
    def titleToNumber(self, s: str) -> int:
        alphabet = string.ascii_uppercase
        d = {letter: index for index, letter in enumerate(alphabet, 1)}
        
        if len(s) == 1:
            return d[s.upper()]
        
        colNumber = 0
        length = len(s) - 1
        
        for letter in s:
            val = (26 ** length) * d[letter.upper()]
            colNumber += val
            length -= 1
            
        return colNumber
        
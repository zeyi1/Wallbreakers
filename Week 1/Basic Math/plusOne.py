"""
Procedure:
Start from the end, everytime we see a 9 replace it with 0, stop until we see the first non 9.
If the index is negative, that means every digits is 9, so prepend a 1 to the list, otherwise increment the value at that index.

Complexity:
n -> length of the input
Time: O(n)
Space: O(1)
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        
        while digits[i] == 9 and i >= 0:
            digits[i] = 0
            i -= 1
        
        if i < 0:
            return [1] + digits
        
        else:
            digits[i] += 1
            return digits
        
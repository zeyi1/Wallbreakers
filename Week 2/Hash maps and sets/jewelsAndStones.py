"""
Procedure:
Use the class Counter to create a dictionary of counts for the stones we have.
Loop the jewels and see if we own it.

Complexity:
s -> length of string S, j -> length of string J
Time: O(max(s, j))
Space: O(s)
"""

from collections import Counter

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        if not J or not S:
            return 0
        
        stones = Counter(S)
        
        jewels = 0
        
        for i in J:
            if i in stones:
                jewels += stones[i]
                
        return jewels
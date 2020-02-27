"""
Procedure:
Check that the length of both strings are equal.
Sort both strings, if at any point the characters at the same index are different then it is not
an anagram.

Complexity:
n -> length of input string
Time: O(nlogn)
Space: O(n)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sortedS, sortedT = sorted(s), sorted(t)
        
        for i in range(len(sortedS)):
            if sortedS[i] != sortedT[i]:
                return False
            
        return True
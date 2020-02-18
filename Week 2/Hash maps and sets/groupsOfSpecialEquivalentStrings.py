"""
Procedure:
Words belonging to the same group will have the same characters with the same even/odd parity (%2).
To form a key that emcompasses them, we can create a new string consisting of allEven + allOdd index characters.
Use a set to count the unique strings.

Complexity:
n -> number of words, m -> length of words
Time: O(n * m log m)
Space: O(n)
"""

class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        if not A:
            return 0
        
        uniqueGroups = set()
        
        for word in A:
            even = sorted(word[0::2])
            odd = sorted(word[1::2])
            key = ''.join(even+odd)
            uniqueGroups.add(key)
        
        return len(uniqueGroups)
        
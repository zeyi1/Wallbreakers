"""
Procedure:
Sort p, and loop s, each time getting a sorted substring of size p, if it equals to p, we found an anagram.

Complexity:
s -> length of s, p -> length of p
Time: O(s * plogp)
Space: O(s * p)
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        slen, plen = len(s), len(p)
        sortedP = sorted(p)
        indices = []
        
        for i in range(slen - plen + 1):
            substring = sorted(s[i:plen+i])
            if substring == sortedP:
                indices.append(i)
                
        return indices
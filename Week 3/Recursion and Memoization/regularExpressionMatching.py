"""
Procedure:
Use a cache where the keys are the index of the word and the index of the pattern,
and the value is whether this is a regular expression matching.
The recurrence for this problem is as follows:
If we encounter a star, and word[i] == pattern[j-1] or pattern[j-1] == '.', there are two scenarios.
1. We compare the current character of word and the character of pattern located 2 
indexes back, this is for 0 occurrences of the star. If this match then it is a
matching. T[i][j-2]
2. Otherwise we check the previous index of word with the character of pattern. T[i-1][j]

If we encounter a dot or the character from word and pattern are the same, then it is a match.
Otherwise is not a match.

Complexity:
n -> length of word, m -> length of pattern
Time: O(m * n)
Space: O(m * n)
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not s and not p:
            return True
        
        return self.helper(s, len(s), p, len(p), {})
        
        
    def helper(self, s, sindex, p, pindex, cache):
        if (sindex, pindex) in cache:
            return cache[(sindex, pindex)]
        
        if pindex == 0:
            return sindex == 0
            
        if p[pindex - 1] == '*':
            if self.helper(s, sindex, p, pindex - 2, cache):
                cache[(sindex, pindex)] = True
                return True
            
            if sindex != 0 and (s[sindex - 1] == p[pindex - 2] or p[pindex - 2] == '.'):
                if self.helper(s, sindex - 1, p, pindex, cache):
                    cache[(sindex, pindex)] = True
                    return True
                
        if sindex != 0 and (s[sindex - 1] == p[pindex - 1] or p[pindex - 1] == '.'):
            if self.helper(s, sindex - 1, p, pindex - 1, cache):
                cache[(sindex, pindex)] = True
                return True
        
        cache[(sindex, pindex)] = False
        
        return False
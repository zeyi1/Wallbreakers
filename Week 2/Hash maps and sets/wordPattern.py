"""
Procedure:
Same as isomorphic strings question.

Complexity:
n -> length of pattern
Time: O(n)
Space: O(n)
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        
        pLen, wLen = len(pattern), len(words)
        
        if pLen != wLen:
            return False
        
        d = {}
        
        for i in range(pLen):
            if pattern[i] not in d:
                if words[i] not in d.values():
                    d[pattern[i]] = words[i]
                    
                else:
                    return False
                
            else:
                if d[pattern[i]] != words[i]:
                    return False
                
        return True
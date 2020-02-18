"""
Procedure:
This question asks for index character mapping, not for actual character mapping.
The characters at s will be the keys and the chars at t will be the values.
At each index, check if the character of s is in the dictionary,
if it is, check if the value equals the character of t.
If it is not, check if the character of t is already mapped to another key.
If both conditions are false then map them.

Complexity:
s -> length of string
Time: O(s)
Space: O(s)
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                if t[i] not in d.values():
                    d[s[i]] = t[i]
                else:
                    return False
                
            else:
                if d[s[i]] != t[i]:
                    return False
                
        return True
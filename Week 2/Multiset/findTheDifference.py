"""
Solution 1

Procedure:
Use a counter for s, for every character in t, if the character is not in s, this is the newly added character,
otherwise decrease the count from counter and if the count is 0, delete it.

Complexity:
n -> length of s
Time: O(n)
Space: O(n)
"""

from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if not s:
            return t
        
        sCounter = Counter(s)
        
        for char in t:
            if char not in sCounter:
                return char
            
            sCounter[char] -= 1
            if sCounter[char] == 0:
                del sCounter[char]
                


"""
Solution 2

Procedure:
Using bitwise xor operation. Start with 0 since anything xor 0 yields anything. And anything xor anything yields 0.
So every duplicate will cancel out, and the remaining character will be the newly added one.

Complexity:
n -> length of s + t
Time: O(n)
Space: O(n) since we create the string s+t
"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if not s:
            return t
        
        result = 0
        
        for char in s+t:
            result ^= ord(char)
            
        return chr(result)
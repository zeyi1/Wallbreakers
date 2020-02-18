"""
Solution 1

Procedure:
Create a counter of the string, loop the string and find the first character that has a count of 1.

Complexity:
n -> length of input string
Time: O(n)
Space: O(n)
"""

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        
        sCounter = Counter(s)
        
        for i, char in enumerate(s):
            if sCounter[char] == 1:
                return i
            
        return -1



"""
Solution 2

Procedure:
Use a set and a dictionary, set will keep track of elements we seen, and the dictionary will contain the character and its index.
If we see duplicates, delete them from the dictionary. Then return the minimum value of the dictionary.

Complexity:
n -> length of input string
Time: O(n)
Space: O(n)
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        
        d, seen = {}, set()
        
        for i, char in enumerate(s):
            if char not in seen:
                d[char] = i
                seen.add(char)
                
            elif char in d:
                del d[char]
                
        return min(d.values()) if d else -1
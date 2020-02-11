"""
Procedure:
Create a dictionary that contains the characters with their counts of one string.
Loop the other string, if at any point the current char is not in the dictionary, return False.
Otherwise, reduce its count and if the count reaches 0, remove it.
Two strings will be anagram if the dictionary becomes empty.

Complexity:
n -> length of string input
Time: O(n)
Space: O(n)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        d = {}
        
        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
                
        for char in t:
            if char not in d:
                return False
            
            d[char] -= 1
            if d[char] == 0:
                del d[char]
                
        return len(d) == 0
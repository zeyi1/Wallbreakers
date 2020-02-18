"""
Solution 1

Procedure:
Create a counter for p. At every index of s, create a counter up to the length of p. And compare both counters. 
This solution is inefficient as we are not reusing information and creating a new counter at each iteration.

Complexity:
n -> length of s, m -> length of p
Time: O(n * m^2)  // since slicing takes m time and creating the counter as well
Space: O(n * m^2)
"""

from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        slen, plen = len(s), len(p)
        pCounter = Counter(p)
        
        indices = []
        
        for i in range(slen - plen + 1):
            j = i + plen
            curCounter = Counter(s[i:j])

            if curCounter == pCounter:
                indices.append(i)
                
        return indices



"""
Solution 2

Procedure:
Create a counter for p, and a counter for s of one size less than p. If counter of p is of size 3, then s would be of size 2.
Loop through every character in s, maintaining a pointer to the beginning (left) and a pointer to the next character to add.
Add the next character into sCounter and compare if both Counters are the same, add left to out result.
Decrease the value of Counter at the leftmost position s[left], and delete it if it reaches 0. Advance the left pointer.

"""

from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        slen, plen = len(s), len(p)
        pCounter = Counter(p)
        sCounter = Counter(s[:plen-1])
            
        indices = []
        left = 0
        
        while left <= slen - plen:
            index = left + plen - 1
            sCounter[s[index]] += 1
            
            if sCounter == pCounter:
                indices.append(left)
                
            sCounter[s[left]] -= 1
            if sCounter[s[left]] == 0:
                del sCounter[s[left]]
                
            left += 1
            
        return indices
            
        
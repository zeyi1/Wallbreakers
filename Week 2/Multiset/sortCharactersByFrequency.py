"""
Procedure:
Use a counter to get all occurrences of each letter. Sort it by descending order.
Create a new list using the character * occurrences.
Join the result

Complexity:
n -> length of the input string
Time: O(nlogn)
Space: O(n)
"""

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        if not s:
            return ""
        
        sCounter = Counter(s)
        sortedList = sorted(sCounter.items(), key=lambda x: x[1], reverse=True)
        
        result = [char*cnt for char, cnt in sortedList]
        
        return ''.join(result)
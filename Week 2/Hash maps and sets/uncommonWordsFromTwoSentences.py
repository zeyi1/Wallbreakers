"""
Procedure:
Use the Counter class, that combines both strings.
Return the words that have count of 1.

Complexity:
n -> length of string input
Time: O(n)
Space: O(n)
"""

from collections import Counter

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        if not A and not B:
            return []
        
        a = Counter(A.split(' '))
        a.update(B.split(' '))
        
        uncommon = [word for word, count in a.items() if count == 1]
        
        return uncommon
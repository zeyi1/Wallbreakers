"""
Procedure:
The subproblem for this problem is when the characters either match or does not match.
If the characters match, just continue with the next index.
If they do not match then the result would be the minimum of 
replace - move both index by 1
insert - maintain same index and decrement the other index
delete - opposite of insert

Complexity:
n -> length of first word, m -> length of second word
Time: O(n * m)
Space: O(n * m)
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return len(word1 or word2)
        
        return self.helper(word1, len(word1), word2, len(word2), {})
        
        
    def helper(self, word1, index1, word2, index2, memo):
        if index1 == 0 or index2 == 0:
            return index1 + index2
        
        if (index1, index2) in memo:
            return memo[(index1, index2)]
        
        minimum = 0
        
        if word1[index1-1] == word2[index2-1]:
            minimum = self.helper(word1, index1-1, word2, index2-1, memo)
        
        else:
            minimum = 1 + min(self.helper(word1, index1-1, word2, index2-1, memo),
                              self.helper(word1, index1, word2, index2-1, memo),
                              self.helper(word1, index1-1, word2, index2, memo))
            
        memo[(index1, index2)] = minimum
        
        return minimum
        
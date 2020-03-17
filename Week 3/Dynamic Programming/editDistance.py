"""
Procedure:
Create a dp table of size len(word1)+1 and len(word2)+1 to account for empty string and
prepopulate the table at index 0 correspondingly, the number of operations will be the 
length of the string when comparing with the empty string.
The recurrence will be dp[i][j] = dp[i-1][j-1] when the characters are equal, otherwise
it will be 1 + the minimum of replace, insert and delete.

Complexity:
n -> length of word1, m -> length of word2
Time: O(m * n)
Space: O(m * n)
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return len(word1 or word2)
        
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        for i in range(m+1):
            dp[i][0] = i
            
        for i in range(n+1):
            dp[0][i] = i
            
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                    
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
                    
                    
        return dp[-1][-1]
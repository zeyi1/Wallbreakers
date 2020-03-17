"""
Procedure:
Create a dp table of size n+1 by m+1 to account for the empty string.
Need to preprocess for empty string if the pattern contains a star, so that it takes the value at
2 indexes back for empty occurrences.

The occurrence is as follows
For star
dp[i][j] = dp[i][j-2] or dp[i-1][j] if p[j-2] == dot or s[i-1] == p[j-2] otherwise dp[i][j-2]
For dot or when the character at s and p match, we just take the value obtain without these characters.

Complexity:
n -> length of s, m -> length of p
Time: O(m * n)
Space: O(m * n)
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not s and not p:
            return True
        
        m, n = len(s), len(p)
        dp = [[False] * (n+1) for _ in range(m+1)]
        
        dp[0][0] = True
        
        for i in range(n):
            if p[i] == '*' and i != 0:
                dp[0][i+1] = dp[0][i-1]
                
                
        for sindex in range(1, m+1):
            for pindex in range(1, n+1):
                if p[pindex-1] == '*' and pindex != 1:
                    if s[sindex-1] == p[pindex-2] or p[pindex-2] == '.':
                        dp[sindex][pindex] = dp[sindex][pindex-2] or dp[sindex-1][pindex]
                    else:
                        dp[sindex][pindex] = dp[sindex][pindex-2]
                        
                elif s[sindex-1] == p[pindex-1] or p[pindex-1] == '.':
                    dp[sindex][pindex] = dp[sindex-1][pindex-1]
                    
        return dp[-1][-1]
        
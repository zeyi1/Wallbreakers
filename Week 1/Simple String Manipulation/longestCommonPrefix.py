"""
Procedure:
Retrieve the shortest string. For every word, check if they start with this string starting from index 1 to n-1.

Complexity:
n -> length of input list
k -> length of shortest string
Time: O(k * n)
Space: O(k)
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = min(strs, key=len)
        longestPrefix = 0
        
        for i in range(1, len(prefix) + 1):
            if not all(word.startswith(prefix[:i]) for word in strs):
                break
                
            longestPrefix = i
            
        return prefix[:longestPrefix]
    

"""
Procedure:
Sort both lists, use the smallest cookie to see if it satisfies the least greedy child.
If it doesn't use the next cookie.

Complexity:
n -> length of longer input list
Time: O(nlogn)
Space: O(n)
"""

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not g or not s:
            return 0
        
        sortedG, sortedS = sorted(g), sorted(s)
        childIndex, cookieIndex = 0, 0
        happyChildren = 0
        
        while cookieIndex < len(s) and childIndex < len(g):
            if sortedS[cookieIndex] >= sortedG[childIndex]:
                happyChildren += 1
                cookieIndex += 1
                childIndex += 1
            
            else:
                cookieIndex += 1
                
        return happyChildren
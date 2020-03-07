"""
Procedure:
Only Odd numbers can have complete binary trees. Use a dictionary where the keys are the
number of nodes, and the values all possible trees at that number.

Complexity:
n -> input N
Time: O(2^n)
Space: O(2^n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N % 2 == 0:
            return []
        
        cache = {1: [TreeNode(0)]}
        
        for i in range(3, N+1, 2):
            temp = []
            for j in range(1, i, 2):
                for left in cache[j]:
                    for right in cache[i-j-1]:
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        temp.append(root)
            cache[i] = temp
            
        return cache[N]
        
        
  
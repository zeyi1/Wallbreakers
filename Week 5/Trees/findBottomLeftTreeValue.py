"""
Procedure:
Traverse level by level, and assign leftmost the first non-empty value.

Complexity:
n -> average number of nodes in each level, h -> height of the tree
Time: O(n*h)
Space: O(n*h)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        stack = [root]
        leftmost = root.val
        
        while stack:
            for node in stack:
                if node:
                    leftmost = node.val
                    break
                    
            stack = [child for node in stack for child in (node.left, node.right) if child]
            
        return leftmost
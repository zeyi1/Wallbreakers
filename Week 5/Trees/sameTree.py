"""
Procedure:
Check level by level, if the values are not equal they are not the same tree.

Complexity:
n -> number of nodes
Time: O(n)
Space: O(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True 
        
        if not p or not q or p.val != q.val:
            return False
        
        stack = [node for node in (p.left, p.right)]
        stack2 = [node for node in (q.left, q.right)]
        
        while stack and stack2:
            
            nodes1, nodes2 = [node.val if node else None for node in stack], [node.val if node else None for node in stack2]
            print(nodes1, nodes2)
            if nodes1 != nodes2:
                return False
            
            stack = [child for node in stack if node for child in (node.left, node.right)]
            stack2 = [child for node in stack2 if node for child in (node.left, node.right)]
            
        return True
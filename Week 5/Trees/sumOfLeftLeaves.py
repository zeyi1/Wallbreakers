"""
Procedure:
Use a stack, the stack will contain a node and a boolean flag indicating if the
node was a left child. 

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
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        stack = [(root, 0)]
        summ = 0
        
        while stack:
            node, left = stack.pop()
            
            if left and not node.left and not node.right:
                summ += node.val
                
            if node.left:
                stack.append((node.left, 1))
                
            if node.right:
                stack.append((node.right, 0))
                
        return summ
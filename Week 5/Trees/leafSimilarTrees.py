"""
Procedure:
A leaf is when a node does not have a left and right children.
Use a stack and loop through the children, always appending the right child first,
this allows every left child to be at the top of the stack, and thus giving
the correct order of leaf nodes.

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
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        l1, l2 = self.findLeaves(root1), self.findLeaves(root2)
        
        return l1 == l2
        
        
    def findLeaves(self, root):
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
                    
            if not node.left and not node.right:
                result.append(node.val)
            
            if node.right:
                stack.append(node.right)
                
            if node.left:
                stack.append(node.left)

        return result
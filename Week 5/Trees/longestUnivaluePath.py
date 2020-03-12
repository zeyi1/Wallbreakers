"""
Procedure:
Similar to diameterOfBinaryTree.py, but now also add the parent value to the stack,
this will help us identify equal numbers.

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
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        depth = {None: 0}
        max_length = 0
        stack = [(root, 0, None)]
        
        while stack:
            node, visited, parent_val = stack.pop()
            
            if not node:
                continue
                
            if not visited:
                stack += [(node, 1, parent_val), (node.left, 0, node.val), (node.right, 0, node.val)]
                
            else:
                if parent_val == node.val:
                    depth[node] = max(depth[node.left], depth[node.right]) + 1
                    
                else:
                    depth[node] = 0
                    
                max_length = max(max_length, depth[node.left] + depth[node.right])
                
                
        return max_length
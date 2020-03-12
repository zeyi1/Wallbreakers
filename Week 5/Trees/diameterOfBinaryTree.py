"""
Procedure:
Use a stack, each element in the stack will contain the node and boolean visited.
Use a dictionary, key will be the node and the value will be depth of the node,
which is calculated by the maximum depth of its left subtree and its right subtree.
If the node was already seen, find from the dictionary its left and right subtree depths,
and calculate the maximum total depth which is the max of the current total depth or 
the sum of the left subtree and the right subtree.

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
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        max_length = 0
        stack = [(root, 0)]
        depth = {None: -1}
        
        while stack:
            node, visited = stack.pop()
            if not node:
                continue
                
            if not visited:
                stack += [(node, 1), (node.left, 0), (node.right, 0)]
                
            else:
                left_depth = depth[node.left] + 1
                right_depth = depth[node.right] + 1
                max_length = max(max_length, left_depth + right_depth)
                depth[node] = max(left_depth, right_depth)
                
        return max_length
        
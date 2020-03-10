"""
Solution 1 - Iteratively

Procedure:
Use a stack and a visited flag and start appending from the rightmost child.
Each time we see a node, append it again but now as visited.
The result will be in post order.

Complexity:
n -> number of nodes
Time: O(2n) -> O(n)
Space: O(n)
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        result, stack = [], [(root, 0)]
        
        while stack:
            node, visited = stack.pop()
            
            if not visited:
                stack.append((node, 1))
                
            else:
                result.append(node.val)
                continue    

            if node.children:
                for children in node.children[::-1]:
                    stack.append((children, 0))          
                
        return result



"""
Solution 2 - Iteratively

Procedure:
Instead of using a flag, go from top to bottom and left to right. 
The stack would contain root -> rightmost -> leftmost, reverse the output list
and it would be in post order traversal.

Complexity:
n -> number of nodes
Time: O(n)
Space: O(n)
"""

"""

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        result, stack = [], [root]
        
        while stack:
            node = stack.pop()
            
            result.append(node.val)

            if node.children:
                for children in node.children:
                    stack.append(children)          
                
        return result[::-1]
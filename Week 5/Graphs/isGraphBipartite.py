"""
Procedure:
Use a dictionary representing the nodes as colors, each neighbor must have a different color
than the current node. If any neighbor has the same color then the graph is not bipartite.

Complexity:
n -> number of nodes
Time: O(n)
Space: O(n)
"""

from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        
        for node in range(len(graph)):
            if node not in color:
                color[node] = 1 
                queue = deque([node])
                
                while queue:
                    curNode = queue.popleft()
                    
                    for neighbour in graph[curNode]:
                        if neighbour not in color:
                            color[neighbour] = color[curNode] ^ 1
                            queue.append(neighbour)
                            
                        elif color[neighbour] == color[curNode]:
                            return False
                        
        return True
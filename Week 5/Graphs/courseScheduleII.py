"""
Procedure:
Same idea as Course Schedule, add first all class with 0 indegrees, and all
subsequent ones that become 0. Return the reverse.

Complexity:
v = number of courses, e = number of pairs
Time: O(v + e)
Space: O(v + e)
"""

from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:set() for i in range(numCourses)}
        inDegree = {i:0 for i in range(numCourses)}
        
        for c1, c2 in prerequisites:
            graph[c1].add(c2)
            inDegree[c2] += 1
            
        queue = deque()
        visited = set()
        result = []
        
        for c, indegree in inDegree.items():
            if indegree == 0:
                queue.append(c)
                
        while queue:
            curClass = queue.popleft()
            result.append(curClass)
            visited.add(curClass)
            
            for prerequisite in graph[curClass]:
                inDegree[prerequisite] -= 1
                
                if inDegree[prerequisite] == 0:
                    queue.append(prerequisite)
         
        if len(visited) == numCourses:
            return result[::-1]
        
        else:
            return []
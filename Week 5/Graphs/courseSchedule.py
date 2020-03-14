"""
Procedure:
Construct the graph as a dictionary the key will be the course number and the value will be a container.
Construct another dictionary, that will contain the number of incoming edges (the prerequisite courses).
Use a queue, and add only the courses that are not prerequisites (in-degree == 0).
The idea is to loop every course c in the queue, and for each prerequisite course this course has, remove
the in-degree c from the prerequisite. If the in-degree of the prerequisite reaches 0, add it to the queue.
Use a set to keep track of all the course seen, which will only be the ones with in-degree 0.

Complexity:
v = number of courses, e = number of pairs
Time: O(v + e)
Space: O(v + e)
"""

from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {i: set() for i in range(numCourses)}
        in_degrees = {i:0 for i in range(numCourses)}
        
        for edge in prerequisites:
            graph[edge[0]].add(edge[1])
            in_degrees[edge[1]] += 1
        
        queue = deque()
        visited = set()
        
        for index, in_degree in in_degrees.items():
            if in_degree == 0:
                queue.append(index)
                
        while queue:
            index = queue.popleft()
            visited.add(index)
            for g in graph[index]:
                in_degrees[g] -= 1
                if in_degrees[g] == 0:
                    queue.append(g)
                    
        return len(visited) == numCourses
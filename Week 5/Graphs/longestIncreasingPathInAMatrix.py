"""
Procedure:
Use Topological Sort, create a dictionary key as coordinates and values as number of indegrees
which is all neighbors that are greater than the current coordinate.
Initialize a queue with all coordinates that have 0 indegrees.
Use BFS and increment the longest path level by level, the initial queue means the ending numbers
of a possible path, so the next level will be the second possible numbers, etc.
To achieve this, loop through the length of the current queue, and add all other indegrees that
reaches 0 during the process.

Complexity:
n -> number of rows, m -> number of columns
Time: O(m*n)
Space: O(m*n)
"""

from collections import deque

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or len(matrix[0]) == 0:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        directions = ((1,0), (-1,0), (0,1), (0,-1))
        longestPath = 0
        indegree = {}
        queue = deque()
        
        for i in range(m):
            for j in range(n):
                indegree[(i, j)] = 0
                
                for x, y in directions:
                    newx, newy = i+x, j+y
                    
                    if 0 <= newx < m and 0 <= newy < n and matrix[newx][newy] > matrix[i][j]:
                        indegree[(i,j)] += 1
            

        for key, val in indegree.items():
            if val == 0:
                queue.append(key)
                

        while queue:
            length = len(queue)
            
            for i in range(length):
                x, y = queue.popleft()
                
                for x1, y1 in directions:
                    newx, newy = x+x1, y+y1
                    
                    if 0 <= newx < m and 0 <= newy < n and matrix[newx][newy] < matrix[x][y]:
                        indegree[(newx, newy)] -= 1
                        
                        if indegree[(newx, newy)] == 0:
                            queue.append((newx, newy))
                            
            longestPath += 1

            
        return longestPath
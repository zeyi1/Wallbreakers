"""
Procedure:
Students are represented as rows and students' friends are the column values that are 1 in that row.
Loop through all students, for each use DFS on the friends, and add all these friends as visited, 
so that when we reach a new student that is not friends with the previous ones, we can get a new circle.

Complexity:
m -> number of rows, n -> number of elements in each row
Time: O(m * n)
Space: O(n)
"""

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M or len(M[0]) == 0:
            return 0
        
        rowNum, friendCircles = len(M), 0
        visited, stack = set(), []
        
        for i in range(rowNum):
            if i not in visited:
                stack.append(i)
                
                while stack:
                    curStudent = stack.pop()
                    if curStudent not in visited:
                        visited.add(curStudent)
                        for j, val in enumerate(M[curStudent]):
                            if val == 1 and j not in visited:
                                stack.append(j)
                                
                friendCircles += 1
                
        return friendCircles
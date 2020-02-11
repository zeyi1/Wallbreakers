"""
Procedure:
Get all the coordinates where the value is 1.
Use DFS for each location, the stopping point would be when the neighbor is 0.
And use a set to keep track of visited coordinates, and only look for coordinates we have not visited yet.

Complexity:
m -> number of rows, n -> number of element in a row
Time: O(m * n)
Space: O(m * n)
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid[0]) == 0:
            return 0
        
        rowNum, colNum = len(grid), len(grid[0])
        stack, visited = [], set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        startPoints = [(i,j) for i in range(rowNum) for j in range(colNum) if grid[i][j] == '1']
        islands = 0
        
        for coord in startPoints:
            if coord not in visited:
                stack.append(coord)
                islands += 1
                while stack:
                    x, y = stack.pop()
                    visited.add((x, y))

                    for i, j in directions:
                        newx, newy = x+i, y+j
                        if 0 <= newx < rowNum and 0 <= newy < colNum and grid[newx][newy] == '1' and (newx, newy) not in visited:
                            stack.append((newx, newy))
                         
        return islands
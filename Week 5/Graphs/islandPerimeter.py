"""
Procedure:
Find the first 1 and add its coordinates to the stack and change the value to 2.
For all neighbors if they are either 0 or out-of-bounds increment the perimeter,
if they are 1's add it to the stack and change its value to 2.

Complexity:
m -> number of rows, n -> number of columns
Time: O(n * m)
Space: O(n * m)
"""

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or len(grid[0]) == 0:
            return 0
        
        directions = [(1,0), (0,1),(-1,0),(0,-1)]
        m, n = len(grid), len(grid[0])
        flag = False
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    stack = [(i, j)]
                    grid[i][j] = 2
                    flag = True
                    break
            if flag:
                break
        
        perimeter = 0
        
        while stack:
            x, y = stack.pop()
            
            for i, j in directions:
                newx, newy = i+x, j+y
                if newx < 0 or newy < 0 or newx == m or newy == n or grid[newx][newy] == 0:
                    perimeter += 1
                    
                elif grid[newx][newy] == 1:
                    grid[newx][newy] = 2
                    stack.append((newx, newy))
                    
                    
        return perimeter
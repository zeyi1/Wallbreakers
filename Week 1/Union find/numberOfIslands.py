"""
Solution 1

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



"""
Solution 2

Procedure:
Create UnionFind object and initialize it with (lengthOfRows * lengthOfColumns). 
Loop through the entire matrix, if the current location is '1', check the next locations.
If the current location is '0', increment a zero count since we will never access these indexes.
We only need to the down and right for the next locations, since we are looping forward.
If the next location is also '1', get its corresponding index so that we can find it in out UnionFind object.
currentIndex = i * numberOfColumns + j
nextIndex = i+1 * numberOfColumns + j  or  i * numberOfColumns + j + 1
Find if they do not belong to the same set, if thats the case union them.
The numberOfIslands will be the (setCounts - zeroCounts).

Complexity:
m -> number of rows, n -> number of columns in the row
Time: O(m * n)
Space: O(m * n)
"""

class UnionFind:
    def __init__(self, numSize):
        self.parents = [i for i in range(numSize)]
        self.size = [1 for _ in range(numSize)]
        self.count = numSize
    
    
    def findRoot(self, num):
        while self.parents[num] != num:
            self.parents[num] = self.parents[self.parents[num]]
            num = self.parents[num]
            
        return num
    
    
    def union(self, x, y):
        rootX, rootY = self.findRoot(x), self.findRoot(y)
        if rootX == rootY:
            return
        
        if self.size[rootX] < self.size[rootY]:
            self.parents[rootX] = self.parents[rootY]
            self.size[rootY] += self.size[rootX]
            self.size[rootX] = 0
            
        else:
            self.parents[rootY] = self.parents[rootX]
            self.size[rootX] += self.size[rootY]
            self.size[rootY] = 0
            
        self.count -= 1
            
            
    def find(self, x, y):
        if self.parents[x] == self.parents[y]:
            return True
        
        return False
    
    
    def getSetsCount(self):
        return self.count

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid[0]) == 0:
            return 0
        
        rowNum, colNum = len(grid), len(grid[0])
        numOfIslands = 0
        directions = [(1, 0), (0, 1)]
        
        uf = UnionFind(rowNum*colNum)
        zeroCount = 0

        for i in range(rowNum):
            for j in range(colNum):
                if grid[i][j] == '1':
                    index = i*colNum + j
                    for x, y in directions:
                        newX, newY = i+x, j+y
                        if 0 <= newX < rowNum and 0 <= newY < colNum and grid[newX][newY] == '1':
                            neighborIndex = newX*colNum + newY
                            if not uf.find(index, neighborIndex):
                                uf.union(index, neighborIndex)
                else:
                    zeroCount += 1
        
        numOfIslands = uf.getSetsCount() - zeroCount

        return numOfIslands
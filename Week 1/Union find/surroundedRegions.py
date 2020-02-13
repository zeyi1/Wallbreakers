"""
Solution 1

Procedure:
Find all O that are in the border. 
Perform DFS on them to find connected Os, and change their value to anything to distinguish between the ones that
need to be changed into X.

Complexity:
m -> number of rows, n -> number of elements in a row
Time: O(m * n)
Space: O(m * n)
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or len(board[0]) == 0:
            return
        
        rowNum, colNum = len(board), len(board[0])
        
        if rowNum<=2 or colNum<=2:
            return
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        startPoints = []
        
        for i in range(rowNum):
            if board[i][0] == 'O':
                startPoints.append((i, 0))
                
            if board[i][colNum-1] == 'O':
                startPoints.append((i, colNum-1))
                
        for i in range(1, colNum-1):
            if board[0][i] == 'O':
                startPoints.append((0, i))
                
            if board[rowNum-1][i] == 'O':
                startPoints.append((rowNum-1, i))
        
        while startPoints:
            x, y = startPoints.pop()
            board[x][y] = 'N'
            
            for i, j in directions:
                newx, newy = x+i, y+j
                if 0 <= newx < rowNum and 0 <= newy < colNum and board[newx][newy] == 'O':
                    startPoints.append((newx, newy)) 
                        
        for i in range(rowNum):
            for j in range(colNum):
                if board[i][j] == 'N':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'



"""
Solution 2

Procedure:
Create a UnionFind object and initialize with (lengthOfRows * lengthOfColumns) + 1, the extra element will be
used as the root.
Loop through the border of the matrix and union every 'O' with the extra element. Also, append it to a list.
Loop this list, the idea is to connect every neighbor 'O' (UDLR) with the set we previously connected.
First we find and check if both root are the same, so that we do not traverse multiple times, if they are different
union them and append to the list.
Loop through the entire matrix and only change the 'O's that do not belong to the extra element set to 'X'.

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
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or len(board[0]) == 0:
            return
        
        rowNum, colNum = len(board), len(board[0])
        
        if rowNum<=2 or colNum<=2:
            return
        
        matrixSize = rowNum * colNum
        uf = UnionFind(matrixSize + 1)
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        startPoints = []
        
        for i in range(rowNum):
            if board[i][0] == 'O':
                index = i*colNum
                border.add(index)
                uf.union(matrixSize, index)
                startPoints.append((i, 0))
                
            if board[i][colNum-1] == 'O':
                index = i*colNum + colNum-1
                border.add(index)
                uf.union(matrixSize, index)
                startPoints.append((i, colNum-1))
                
        for i in range(1, colNum-1):
            if board[0][i] == 'O':
                border.add(i)
                uf.union(matrixSize, i)
                startPoints.append((0, i))
                
            if board[rowNum-1][i] == 'O':
                index = (rowNum-1)*colNum + i
                border.add(index)
                uf.union(matrixSize, index)
                startPoints.append((rowNum-1, i))

        while startPoints:
            x, y = startPoints.pop()
            curIndex = x*colNum + y
            
            for i, j in directions:
                newx, newy = x+i, y+j
                if 0 <= newx < rowNum and 0 <= newy < colNum and board[newx][newy] == 'O':
                    newIndex = newx*colNum +newy
                    if not uf.find(curIndex, newIndex):
                        uf.union(curIndex, newIndex)
                        startPoints.append((newx, newy)) 
                        
        for i in range(rowNum):
            for j in range(colNum):
                if board[i][j] == 'O':
                    index = i*colNum + j
                    if not uf.find(matrixSize, index):
                        board[i][j] = 'X'
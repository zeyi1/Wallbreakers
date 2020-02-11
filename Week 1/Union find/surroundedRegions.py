"""
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
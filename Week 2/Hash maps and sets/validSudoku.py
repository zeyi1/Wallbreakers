"""
Procedure:
Using 2 passes, first pass will check every row and column for duplicates using sets and ignoring '.'
The second pass will check duplicates in every square, the starting index of squares are
(0, 0), (0, 3), (0, 6)
(3, 0), (3, 3), (3, 6)
(6, 0), (6, 3), (6, 6)
So, for each start index, loop 3 times horizontally and vertically to get the other values within a square.

Complexity:
m -> number of rows, n -> number of elements in each row
Time: O(m * n)
Space: O(max(m, n))
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowNum, colNum = len(board), len(board[0])
        
        for i in range(rowNum):
            rowSet, colSet = set(), set()
            for j in range(colNum):
                x, y = board[i][j], board[j][i]
                if x != '.':
                    if x in rowSet:
                        return False
                    rowSet.add(x)
                    
                if y != '.':
                    if y in colSet:
                        return False
                    colSet.add(y)
                    
        squaresIndex = (0, 3, 6)
        
        for startX in squaresIndex:
            for startY in squaresIndex:
                squareSet = set()
                for i in range(startX, startX+3):
                    for j in range(startY, startY+3):
                        cell = board[i][j]
                        if cell != '.':
                            if cell in squareSet:
                                return False
                            squareSet.add(cell)
                            
        return True
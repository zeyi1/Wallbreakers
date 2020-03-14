"""
Procedure:
Get the coordinates of the letters that equal the first letter of the word we trying to find.
Use DFS, the stack will contain coordinates, index for the next letter, and backtrack boolean,
this boolean is needed because other paths can reach this position, the backtrack will help us
remove the coordinates from the visited set.

Complexity:
m -> number of rows, n -> number of columns
Time: O(m * n)
Space: O(m * n)
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or len(board[0]) == 0:
            return False
        
        if not word:
            return True
        
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        m, n = len(board), len(board[0])
        
        startPoints = [(i, j) for i in range(m) for j in range(n) if board[i][j] == word[0]]
        length = len(word)
        
        for i, j in startPoints:
            stack = [(i, j, 0, 0)]
            visited = set()
            
            while stack:
                x, y, index, backtrack = stack.pop()
                         
                if backtrack:
                    visited.remove((x, y))
                    continue
                    
                visited.add((x, y))
                stack.append((x, y, index, 1))
                
                if index == length - 1:
                    return True
                
                for tempx, tempy in directions:
                    newx, newy = tempx+x, tempy+y
                    
                    if 0 <= newx < m and 0 <= newy < n and (newx, newy) not in visited and board[newx][newy] == word[index+1]:
                        stack.append((newx, newy, index+1, 0))
                        
        return False
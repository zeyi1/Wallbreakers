"""
Procedure:
Create a Trie data structure with insert (for the available words), startswith (to perform dfs) and DFS (to find all words).
Use DFS on every value of the matrix and every complete iteration will have a seen set because we are starting from new at
every cell, also we need to backtrack at each iteration to clear nodes we seen that were reached from other cells. 
Use startswith so that we dont check irrelevant cells and only check prefixes that are in the Trie.

Complexity:
n -> number of rows, m -> number of cols, s -> length of average word, l -> number of words
Time: O(n * m * 4^s)
Space: O(max(s * l, 4^s))
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.leaf = False
        
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
        
    def insert(self, word):
        node = self.root
        
        for char in word:
            if char not in node.children:
                nextNode = TrieNode()
                node.children[char] = nextNode
                node = nextNode
                
            else:
                node = node.children[char]
                
        node.leaf = True
        

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            
            node = node.children[char]
            
        return True
    
    
    def DFS(self, board, words, m, n):
        result = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for x in range(m):
            for y in range(n):
                prefix = board[x][y]
                stack = [(x, y, prefix, False)]
                seen = set()

                while stack:
                    i, j, s, backtrack = stack.pop()
                    
                    if s in words:
                        result.add(s)

                    if backtrack:
                        seen.remove((i, j))
                        continue    

                    seen.add((i, j))
                    stack.append((i, j, s, True))

                    if self.startsWith(s):
                        for x2, y2 in directions:
                            newX, newY = i + x2, j + y2
                            if 0 <= newX < m and 0 <= newY < n and (newX, newY) not in seen:
                                temp = s + board[newX][newY]
                                if self.startsWith(temp):
                                    stack.append((newX, newY, temp, False))
                                
        return result       
        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or len(board[0]) == 0 or not words:
            return []
        
        rowNum, colNum = len(board), len(board[0])
        root = Trie()
        setWords = set(words)
        
        for word in words:
            root.insert(word)            
        
        return root.DFS(board, setWords, rowNum, colNum)
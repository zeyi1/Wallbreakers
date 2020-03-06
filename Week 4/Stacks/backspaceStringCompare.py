"""
Procedure:
Use a stack, if the character is # pop from the stack, otherwise add the character.

Complexity:
n -> length of input list
Time: O(n)
Space: O(n)
"""

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.helper(S) == self.helper(T)
        
        
    def helper(self, string):
        stack = []
        
        for char in string:
            if char == '#':
                if stack:
                    stack.pop()
                    
            else:
                stack.append(char)
                
        return stack
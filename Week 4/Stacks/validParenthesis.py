"""
Procedure:
Use a stack, push to the stack for any open parenthesis.
If a close parenthesis is encountered pop from the stack and compare if its the same type.
A valid parenthesis will be when our stack is empty at the end of the iteration.

Complexiy:
n -> length of input string
Time: O(n)
Space: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        stack = []
        
        for char in s:
            if char in '([{':
                stack.append(char)
                
            elif stack:
                openP = stack.pop()
                if openP == '(' and char != ')':
                    return False

                elif openP == '[' and char != ']':
                    return False

                if openP == '{' and char != '}':
                    return False
                    
            else:
                return False
            
        return len(stack) == 0
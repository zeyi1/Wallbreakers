"""
Procedure:
Use a stack, if an open parenthesis is encountered, append 0 to the stack.
Otherwise, the value of a close parenthesis must be at least 1, so it would be
max(stack[-1] * 2, 1)

Complexity:
n -> length of input string
Time: O(n)
Space: O(n)
"""

class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0]
        
        for paren in S:
            if paren == '(':
                stack.append(0)
                
            else:
                curVal = stack.pop()
                stack[-1] += max(curVal * 2, 1)
                
        return stack.pop()
                
    
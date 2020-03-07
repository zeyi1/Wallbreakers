"""
Procedure:
Use recursion
Base case when both open parenthesis and close parenthesis reach 0
Putting a close parenthesis only when the number of open parenthesis is smaller

"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        openP, closeP = n, n
        self.generate(result, [], openP, closeP)

        return result
        
    def generate(self, result, tempList, openP, closeP):
        if openP == 0 and closeP == 0:
            result.append(''.join(tempList))
            return
        
        if openP > 0:
            self.generate(result, tempList + ['('], openP-1, closeP)
            
        
        if closeP > openP and closeP > 0:
            self.generate(result, tempList + [')'], openP, closeP-1)
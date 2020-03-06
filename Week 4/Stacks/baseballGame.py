"""
Procedure:
Use a stack to keep track of each number along with the current sum.

Complexity:
n -> length of input list
Time: O(n)
Space: O(n)
"""

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        if len(ops) == 1:
            return int(ops[0])
        
        
        stack = [(int(ops[0]), int(ops[0]))]
        
        for s in ops[1:]:
            if s[-1].isdigit():
                num = int(s)
                if stack:
                    summ = stack[-1][1] + num
                else:
                    summ = num
                stack.append((num, summ))
                
            elif s == "C":
                stack.pop()
                
            elif s == "D":
                num, summ = stack.pop()
                newNum = num * 2
                newSum = summ + newNum
                stack.extend([(num, summ), (newNum, newSum)])
                
            else:
                num, summ = stack.pop()
                num2, summ2 = stack.pop()
                num3 = num + num2
                newSum = summ + num3
                stack.extend([(num2, summ2), (num, summ), (num3, newSum)])
                
        return stack[-1][-1]
                
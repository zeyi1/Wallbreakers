"""
Procedure:
Sort the list so that is easier to code the logic.
The stack will contain the current sum, index, and curNumbers.
The index is used for backtracking to allow adding the same element.

Complexity:
n -> length of input list, k -> single element
Time: O((n + k)!)
Space: O((n + k)!)
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        
        candidates.sort()
        stack = [(0, 0, [])]
        result = []
        
        while stack:
            summ, index, curList = stack.pop()
            
            if summ == target:
                result.append(curList)
                continue
                
            for i in range(index, len(candidates)):
                curSum = summ + candidates[i]
                
                if curSum > target:
                    break
                    
                stack.append((curSum, i, curList + [candidates[i]]))
                
        return result
            
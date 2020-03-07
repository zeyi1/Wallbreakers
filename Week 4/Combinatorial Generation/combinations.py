"""
Procedure:
Use the subset idea, and just append to the result if the length of the current list equals k.

Complexity:
n -> input n
Time: O(n * 2^n)
Space: O(n choose k)
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k > n:
            return []
        
        if k == n:
            return [list(range(1,n+1))]
        
        result = [[]]
        combinations = []
        
        for i in range(1, n+1):
            temp = []
            
            for currentList in result:
                newList = currentList + [i]
                if len(newList) == k:
                    combinations.append(newList)
                    
                else:
                    temp.append(newList)
                
            result.extend(temp)
                
                
        return combinations
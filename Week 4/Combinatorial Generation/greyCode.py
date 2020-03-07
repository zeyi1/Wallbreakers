"""
Procedure:
Shifting a number by 1 bit will always cause that number to differ in 1 bit.

Complexity:
n -> input n
Time: O(2**n)
Space: O(2**n)
"""

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n < 0:
            return []
        
        if n == 0:
            return [0]
        

        result = [0, 1]
        
        for num in range(2, 2**n):
            result.append(num ^ (num >> 1))
            
        return result
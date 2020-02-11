"""
Procedure:
Keep dividing the number by 2, if at any step number % 2 is not 0 then it is not a power of 2.

Complexity:
n -> number
Time: O(log base 2(n))
Space: O(1)
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        
        while n != 1:
            if n % 2 != 0:
                return False
            
            n //= 2
            
        return True
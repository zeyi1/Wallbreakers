"""
Procedure:
Create 2 lists to store the sub-solutions, one will contain the actual value of the powers and the
other will contain the exponent.
EX: 5^10 = 5^8 * 5^2
    5^8 = (5^4)^2
    5^4 = (5^2)^2
    5^2 = 5*5

Then use a greedy approach to retrieve the greatest possible value first.

Complexity:
n -> exponent
Time: O(log n)
Space: O(log n)
"""

import math

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n == 1:
            return x
        
        if n == -1:
            return 1/x
        
        
        flag = False
        
        if n < 0:
            flag = True
            n = -n
            
        lgn = int(math.floor(math.log(n, 2)))
        dp_exponent = [0] * lgn
        dp_base = [0] * lgn
        dp_exponent[0], dp_base[0] = 1, x
        
        for i in range(1, lgn):
            dp_exponent[i] = dp_exponent[i-1] * 2
            dp_base[i] = dp_base[i-1] * dp_base[i-1]
            
        result = 1
        
        for i in range(1, lgn+1):
            while n >= dp_exponent[-i]:
                result *= dp_base[-i]
                n -= dp_exponent[-i]
            
            
        return 1/result if flag else result
    
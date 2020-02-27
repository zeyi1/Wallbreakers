"""
Procedure:
Use divide and conquer. 
x^n -> (x*x)^(n/2) if n is even
For odd cases -> x * (x*x)^((n-1)/2)
x^-n -> 1/x ^ n
Base case is when n is 0 -> 1

Complexity:
Time: O(logn)
Space: O(logn)
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n < 0:
            return self.myPow(1/x, -n)
            
        if n % 2:
            return x * self.myPow(x*x, (n-1)//2)
        
        else:
            return self.myPow(x*x, n//2)
        
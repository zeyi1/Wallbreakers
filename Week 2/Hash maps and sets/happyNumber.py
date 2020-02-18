"""
Procedure:
Create a helper function that calculates the sum of the square of the number's digits.
Use a set to keep track of numbers we already seen, if a duplicate appears then a cycle is found.
So the number will never become 1.

Complexity:
n -> number of digits
Time: O(log base 10 (n))
Space: O(log base 10 (n))
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set([n])
        
        while n != 1:
            n = self.sumOfSquares(n)
            if n in seen:
                return False
            seen.add(n)
            
        return True
    
    
    def sumOfSquares(self, n: int) -> int:
        summ = 0
        
        while n != 0:
            lastDigit = n % 10
            summ += (lastDigit**2)
            n //= 10
            
        return summ
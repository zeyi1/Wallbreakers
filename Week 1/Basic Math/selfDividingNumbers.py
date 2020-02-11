"""
Procedure:
Create a helper function that returns whether a number is self dividing. 
Extract the last digit using modulo by 10, if the last digit is 0 or the number % last digit does not equal 0 return False.
Drop the last digit using division by 10.
Return True if the number reaches 0.

Complexity:
n -> number 
r -> right
Time: O(r * log base 10(n)) - log base 10 because at each iteration, the number is reduced by a factor of 10
Space: O(r)
"""

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        def isSelfDividing(num):
            temp = num
            
            while temp != 0:
                lastDigit = temp % 10
                if lastDigit == 0 or num % lastDigit != 0:
                    return False
                
                temp //= 10
                
            return True

                
        return [num for num in range(left, right + 1) if isSelfDividing(num)]
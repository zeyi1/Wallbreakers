"""
Procedure:
The key takeaway in this problem is that the first condition that must be checked is whether the number is divisible by both 3 and 5.

Complexity:
n -> number
Time: O(n)
Space: O(n)
"""

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        if n <= 0:
            return []
        
        result = []
        
        for i in range(1, n + 1):
            if i % 15 == 0:
                result.append('FizzBuzz')
                
            elif i % 3 == 0:
                result.append('Fizz')
                
            elif i % 5 == 0:
                result.append('Buzz')
                
            else:
                result.append(str(i))
                
            
        return result
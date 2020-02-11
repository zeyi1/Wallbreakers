"""
Solution 1 - Using extra memory

Procedure:
Create a list of the same size as the input, and 2 pointers (left, right) that point to the beginning and end of the list respectively.
At each iteration, check whether the number is even or odd.
If the number is even, put the number at where left points to and increment left.
If the number is odd, put the number at where right points to and decrement right.

Complexity:
n -> length of the input list
Time - O(n)
Space - O(n)
"""

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if not A:
            return []
        
        length = len(A)
        parityArray = [-1 for _ in range(length)]
        left, right = 0, length - 1
        
        for num in A:
            if num % 2 == 0:
                parityArray[left] = num
                left += 1
            else:
                parityArray[right] = num
                right -= 1
                
        return parityArray



"""
Solution 2 - In place swapping

Procedure:
Use 2 pointers (left, right) that point to the beginning and end of the list respectively.
Increment left until it points to an odd number and making sure left < right to avoid pointing to already swapped elements
or going overboundary and swapping wrong elements.
Decrement right until it points to an even number and making sure left < right.
Swap the values at index left with index right.

Complexity:
n -> length of the input list
Time - O(n)
Space - O(1)
"""

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if not A:
            return []
        
        length = len(A)
        left, right = 0, length - 1
        
        while left < right:

            while A[left] % 2 != 1 and left < right:
                left += 1
            
            while A[right] % 2 != 0 and left < right:
                right -= 1
                
            A[left], A[right] = A[right], A[left]
            left, right = left + 1, right - 1
            
        return A
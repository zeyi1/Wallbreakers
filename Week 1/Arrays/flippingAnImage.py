"""
Solution 1 - Using extra memory

Procedure:
Reverse each row, and for each number in the row perform either of the following operations to invert the number:
Integer -> 1 - number
Bitwise XOR -> 1 ^ number
Append the row to the return list.

Complexity:
m -> number of rows, n -> number of elements in each row
Time: O(m * n)
Space: O(m * n)
"""

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        if not A or len(A[0]) == 0:
            return []
        
        resultImage = []

        for row in A:
            tempRow = []
            for num in row[::-1]:
                tempRow.append(num^1)
                
            resultImage.append(tempRow)
            
        return resultImage



"""
Solution 2 - In place swapping

Procedure:
For each row, use two pointers (left, right) to point to the beginning and end respectively.
Invert both numbers and swap them until left <= right.

Complexity:
m -> number of rows, n -> number of elements in each row
Time: O(m * n/2) -> O(m * n)
Space: O(1)
"""

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        if not A or len(A[0]) == 0:
            return []
        
        rowNum = len(A)
        
        for i in range(rowNum):
            left, right = 0, len(A[i]) - 1
            
            while left <= right:
                A[i][left], A[i][right] = A[i][right] ^ 1, A[i][left] ^ 1
                left, right = left + 1, right - 1      
        
        return A
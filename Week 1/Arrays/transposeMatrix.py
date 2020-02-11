"""
Solution 1

Procedure:
In Python, using asterik (*) before a container will unpack its content. So, in a matrix, *matrix will unpack it into rows.
There is a built-in function called zip, which combines multiple lists into an iterator of tuples, each tuple contains the values 
of each list at the same index. If the lists are of different size, it combines them based on the shortest list.
So, zip(*matrix) will take the column values of matrix and represent them as rows, which is essentially the transpose of a matrix.

Complexity:
m -> number of rows, n -> number of elements in the shortest row
Time: O(m * n)
Space: O(m * n)
"""

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        if not A or len(A[0]) == 0:
            return []
        
        return list(zip(*A))



"""
Solution 2

Procedure:
Given the case zip is not allowed.
Calculate the minimum length of all rows, this indicates the column index boundary.
At each iteration, get the column values as a list and append it to the result.

Complexity:
m -> number of rows, n -> number of elements in the shortest row
Time: O(m * n)
Space: O(m * n)
"""

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        if not A or len(A[0]) == 0:
            return []
        
        transposed = []
        minLength = min(len(row) for row in A)
        rowNum = len(A)
        
        for i in range(minLength):
            col = []
            for j in range(rowNum):
                col.append(A[j][i])
                
            transposed.append(col)
            
        return transposed

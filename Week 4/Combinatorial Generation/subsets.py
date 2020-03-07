"""
Procedure:
Start with a list of lists, as empty list will always be considered.
Sort the numbers.
For each number, add it to all current lists in our result.
Ex: [1,2,3]
[[]]  ->  [[], [1]] -> [[], [1], [2], [1,2]] ...

Complexity:
n -> length of input array
Time: O(n * 2^n)
Space: O(2^n)
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [nums]
        
        result = [[]]
        
        for num in sorted(nums):
            temp = []
            for currentList in result:
                newList = currentList + [num]
                temp.append(newList)
            
            result.extend(temp)

            
        return result
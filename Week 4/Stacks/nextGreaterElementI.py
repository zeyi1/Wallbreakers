"""
Procedure:
Initialize a stack and a dictionary.
Loop through every element, 
while stack and stack[-1] < num will populate the dictionary with all numbers in the stack that
are less than the current number

Complexity:
n -> length of nums2
Time: O(n)
Space: O(n)
"""

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1:
            return []
        
        stack, d = [], {}
        
        for num in nums2:
            while stack and stack[-1] < num:
                d[stack[-1]] = num
                stack.pop()
                
            stack.append(num)
            
        result = []
        
        for num in nums1:
            result.append(d.get(num, -1))
            
        return result
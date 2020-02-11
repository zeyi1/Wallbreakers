"""
Procedure:
A XOR by 0 gives A, and A XOR A gives 0.
Start with 0 and XOR every number in the list.
Every pair will yield 0 and the single number XOR 0 will yield the single number.

Complexity:
n -> length of input array
Time: O(n)
Space: O(1)
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        singleNum = 0
        
        for num in nums:
            singleNum ^= num
            
        return singleNum
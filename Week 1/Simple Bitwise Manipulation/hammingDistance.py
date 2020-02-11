"""
Procedure:
Loop until both x and y are 0 by right shifting them by 1 at each iteration.
Extract the MSB of each by using & 1, and ^ both MSBs to check whether they are different. If they are, we add 1 to the hamming distance.
Hamming distance is initially 0, the way to add is by calculating first if there is a carry, by using hamming distance & 1.
Then, using hamming distance ^ 1, this give us the actual sum without carry.
If carry is True, loop until it becomes 0, we left shift it by 1 because that is the position we want to add, also we need to calculate the next carry if any.
So, next carry is calculated by hamming distance & carry, and we need to add the previous carry to hamming distance using ^.

Complexity:
n -> number of bits of max(x, y)
Time: O(log base 2(n))
Space: O(1)
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        hamDist = 0
        
        while x != 0 or y != 0:
            msbX = x & 1
            msbY = y & 1
            diffBit = msbX ^ msbY
            
            if diffBit:
                carry = hamDist & diffBit
                hamDist ^= diffBit
                while carry:
                    carry <<= 1
                    previousCarry = carry
                    carry &= hamDist
                    hamDist ^= previousCarry
                
            x, y = x >> 1, y >> 1
            
        return hamDist
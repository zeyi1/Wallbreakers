"""
Procedure:
To invert a single bit we can use XOR 1, since 1 xor 1 = 0 and 0 xor 1 = 1. Therefore, we need a mask of the same size as the input number with 1 in all of its bits.
Loop until the input number is 0, this will give us the position of the set leftmost bit.
Keep shifting the number right by 1 (same as dividing by 2 and removing the rightmost bit)
The mask will be initially 0 and at each iteration will be left shifted by 1 and OR by 1.
By left shifting, the mask will hold 1 at the correct bit, and OR 1 will always set the rightmost bit.

The number complement will then be the XOR of mask with the input number.

Complexity:
n -> number of bits
Time: O(log base 2(n))
Space: O(1)
"""

class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1
        
        mask = 0
        tempNum = num
        
        while tempNum != 0:
            mask <<= 1
            mask |= 1
            tempNum >>= 1
            
        return (mask ^ num)
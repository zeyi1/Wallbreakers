"""
Procedure:
Use & 1 and shift right 1 to get a set bit, and a flag to indicate the first 1 we see. 
Keep incrementing the count, if another 1 appears, cache this count and reset it to 0.

Complexity:
n -> number of bits
Time: O(log base 2(n))
Space: O(1)
"""

class Solution:
    def binaryGap(self, N: int) -> int:
        if N < 3:
            return 0
        
        flag = False
        curDist, maxDist = 0, 0
        
        while N != 0:
            setBit = N & 1
            
            if setBit and not flag:
                flag = True
                N >>= 1
                continue

            if flag:
                curDist += 1
                if setBit:
                    maxDist = max(maxDist, curDist)
                    curDist = 0        
                
            N >>= 1
            
        return maxDist
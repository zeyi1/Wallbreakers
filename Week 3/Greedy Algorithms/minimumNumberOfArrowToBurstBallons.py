"""
Procedure:
Sort the coordinates by ending point. Use a local ending point (the first coordinate), whenever the start point of the next coordinate
is greater than our local ending point, increase the arrows count and set our local ending point to be this new ending point. 
Otherwise, the coordinates have an intersection which means the same arrow can be used.

Complexity:
n -> length of input array
Time: O(nlogn)
Space: O(1)
"""

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points or len(points[0]) == 0:
            return 0
        
        points.sort(key=lambda x: x[1])
        
        curEnd = points[0][1]
        arrows = 1
        
        for newStart, newEnd in points:
            if curEnd < newStart:
                arrows += 1
                curEnd = newEnd
        
        return arrows
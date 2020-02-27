"""
Procedure:
Sort the input list and get a current start and end coordinate. Loop the rest of coordinates,
if the nextStart point is less or equal to our current end point, update end to be the max
of the newEnd point and our current one, otherwise add it to the output list and update our
start and end coordinate.

Complexity:
n -> length of input list
Time: O(nlogn)
Space: O(n)
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or len(intervals[0]) == 0:
            return []
        
        if len(intervals) == 1:
            return intervals
        
        sortedIntervals = sorted(intervals)
        
        start, end = sortedIntervals[0][0], sortedIntervals[0][1]
        result = []
        
        for nextStart, nextEnd in sortedIntervals[1:]:
            if nextStart <= end:
                end = max(end, nextEnd)
                
            else:
                result.append((start, end))
                start, end = nextStart, nextEnd
        
        result.append((start, end))
        
        return result
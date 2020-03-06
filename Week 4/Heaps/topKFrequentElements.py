"""
Procedure:
Create a counter to get each element's frequency. Then create a heap and pop the kth most frequent elements.
Python heapq implementation is for minheap, then to get a maxheap just use the negation of the number.

Complexity:
n -> length of input list
Time: O(klogn)      # Heapify takes O(n), and heappop takes log(n) for each element
Space: O(n)
"""

import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        count = Counter(nums)
        heap = [(-val, key) for key, val in count.items()]
        heapq.heapify(heap)
        result = []
        
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
            
        return result
        
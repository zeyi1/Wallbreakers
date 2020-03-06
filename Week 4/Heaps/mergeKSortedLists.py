"""
Procedure:
Use a heap to store the current value, index, linkedlist. Index is used in case of of matching values.

Complexity:
n -> length of input list, m -> length of average linkedlist
Time: O(n * m * logm)
Space: O(n * m)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        
        merged = dummy = ListNode(0)
        heap = []
        
        for i in range(len(lists)):
            if lists[i]:
                val = lists[i].val
                heapq.heappush(heap, (val, i, lists[i]))
            
        
        while heap:
            val, index, node = heapq.heappop(heap)
            dummy.next = node
            dummy = dummy.next
            node = node.next
            
            if node:
                newVal = node.val
                heapq.heappush(heap, (newVal, index, node))
                
                
        return merged.next
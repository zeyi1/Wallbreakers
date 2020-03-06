"""
Procedure:
Create a pointer to the kth+1 node, so that the head of each group can point to it.
Keep a counter to keep track of kth size nodes.
Loop k times to reverse the nodes in each group.

Complexity:
n -> length of input linked list
Time: O(n * k)
Space: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1:
            return head
        
        dummy = nextHead = ListNode(0)
        dummy.next = head
        prev = cur = head
        
        while True:
            count = 0
            
            while cur and count < k:
                count += 1
                cur = cur.next
                
            if count == k:
                h, t = cur, prev
                for _ in range(k):
                    temp = t.next
                    t.next = h
                    h = t
                    t = temp
                    
                nextHead.next = h
                nextHead = prev
                prev = cur
                
            else:
                return dummy.next
"""
Procedure:
Create 4 nodes
1) Dummy that points to head, to return entire linkedlist
2) Even and odd that points to the second and third node respectively
3) Temp that points to the first odd node

At each iteration,
- Head's next points to odd
- Odd's next points to temp
- Even's next points to the next even
- Even and head increase by 1 while odd increase by 2

Complexity:
n -> length of nodes
Time: O(n)
Space: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        even, odd = head.next, head.next.next
        temp = head.next
        
        while odd:
            head.next = odd
            nextNode = odd.next
            odd.next = temp
            even.next = nextNode
            
            odd = nextNode.next if nextNode else None
            even = even.next
            head = head.next
            
        return dummy.next
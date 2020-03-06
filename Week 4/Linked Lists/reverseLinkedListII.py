"""
Procedure:
Create a dummy to point to head and a node to be the previous before the reverse(newHead).
newHead will remain the same and only newHead.next will keep changing.
Create a tail node, which is used to point to the next node after each swap.
At each iteration,
- Get newHead's next
- Assign newHead's next to be tail's next
- Tail's next becomes the next of its next
- newHead's next next becomes the previous newHead's next

Complexity:
n -> input n
Time: O(n)
Space: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or m == n:
            return head

        count = 1
        dummy = newHead = ListNode(0)
        dummy.next= head
        
        while count != m:
            newHead = newHead.next
            count += 1
            
        tail = newHead.next
        
        while count != n:
            count += 1
            temp = newHead.next
            newHead.next = tail.next
            tail.next = tail.next.next
            newHead.next.next = temp
            
        return dummy.next

"""
Solution 1 - Iteratively
Procedure:
Loop until head is None, at each iteration 
- Save the next node
- Change the current node's next to point to the previous Node
- Previous node becomes the new head
- Advance the current node

Complexity:
n -> length of input linked list
Time: O(n)
Space: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        prev = None
        
        while head:
            nextNode = head.next
            head.next = prev
            prev = head
            head = nextNode 
            
        return prev



"""
Solution 2 - Recursively
Procedure:
Create a helper function, recursively call it with the next node, and current node.

Complexity:
n -> length of input linked list
Time: O(n)
Space: O(n)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self.helper(head)
        
        
    def helper(self, head, prev=None):
        if not head:
            return prev
        
        nextNode = head.next
        head.next = prev
        
        return self.helper(nextNode, head)

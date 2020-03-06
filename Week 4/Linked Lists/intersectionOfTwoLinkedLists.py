"""
Solution 1 - Calculate the length
Procedure:
Retrieve the length of both lists, and move the larger list by the difference of lengths.
Traverse until they point to the same node if any.

Complexity:
n -> length of larger list
Time: O(2n) -> O(n)
Space: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        lenA, lenB = 0, 0
        dummyA, dummyB = headA, headB
        
        
        while dummyA:
            lenA += 1
            dummyA = dummyA.next
            
        while dummyB:
            lenB += 1
            dummyB = dummyB.next
            
        diff = abs(lenA - lenB)
        
        dummyA, dummyB = headA, headB

        if lenA > lenB:
            while diff != 0:
                diff -= 1
                dummyA = dummyA.next
        

        elif lenB > lenA:
            while diff != 0:
                diff -=1
                dummyB = dummyB.next
                
        
        while dummyA and dummyB:
            if dummyA == dummyB:
                return dummyA
            
            dummyA, dummyB = dummyA.next, dummyB.next
            
        return None
                


"""
Solution 2 - Use 2 pointers switching heads
Procedure:
Loop until the nodes are the same, this will be true when both are None or both are the intersected node.
If either one becomes None, then reassign it to be the other head.

Complexity:
n -> length of headA, m -> length of headB
Time: O(n + m)
Space: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        A, B = headA, headB
        
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
            
        return A
        
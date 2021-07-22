# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        # Create new Nodes and a dummy so we can seperate two pointers, dummy.next = head
        dummy = p1 = p2 = ListNode(0, next = head)
        # Check for i in range n and set p1 to p1.next if true
        for i in range(n):
            p1 = p1.next
        # While p1.next exists, move both pointers
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        # Set p2.next to p2.next.next (node we want to remove) then return head
        p2.next = p2.next.next
        # Return head
        return dummy.next
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # While head and head.val are strictly equal to val, point head at head.next
        while head and head.val == val:
            head = head.next
        # if head is not val, return val
        if not head:
            return head
        # Point curr at head
        curr = head
            
        # While current is not None, if curr and curr.next strictly equal val, skip curr.next
        while curr:
            if curr.next and curr.next.val == val:
                curr.next = curr.next.next
            # If not true, dont skip anything
            else:
                curr = curr.next
        # Return head
        return head
        
        
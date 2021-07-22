# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #  Define curr as head, prev as None
        prev = None
        curr = head

        # While loop, ends when curr = None so it know it reached the end of the list
        while curr != None:
            # Set temp to curr.next
            temp = curr.next
            # Point curr.next to previous
            curr.next = prev
            # Point prev at curr
            prev = curr
            # Point curr at temp (which is next)
            curr = temp
            # Since curr would be none, we need to return prev
        return prev
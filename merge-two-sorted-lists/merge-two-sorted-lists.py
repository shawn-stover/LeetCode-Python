# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
       # Checks for l1 being finished and l2 being finished and returning the other list
        if l1 == None: 
            return l2
        if l2 == None:
            return l1
      
        # Make first node the head of l1
        head = l1
        # Check if l1 val > l2 val
        if l1.val > l2.val:
            head = l2
            # After append l2.curr move to next node in l2
            l2 = l2.next
        else:
            # Move to next node in l1
            l1 = l1.next

        # Make current list node the head of the list
        curr = head
        # While l1 and l2 are not None
        while l1 != None and l2 != None:
            # Check if l1.val < l2.val
            if l1.val < l2.val:
                # Point curr.next to l1 and make l1 = l1.next
                curr.next = l1
                l1 = l1.next
            else: 
                # Point curr.next to l2 and make l2 = l2.next
                curr.next = l2
                l2 = l2.next
            # Set curr to curr.next after if-else
            curr = curr.next  
         # If l1 == None curr.next points to l2
        if l1 == None:
            curr.next = l2
        # If l1 != None then curr.next points to l1
        else: 
            curr.next = l1
        # return head
        return head    
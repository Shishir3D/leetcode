# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_pointer = None
        curr_pointer = head

        while curr_pointer is not None:
            next_pointer = curr_pointer.next #stores '2' node's link in the first iteration
            curr_pointer.next = prev_pointer #makes '1' as the last node by making the '1' node point None
            prev_pointer = curr_pointer
            curr_pointer = next_pointer

        return prev_pointer            


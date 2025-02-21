class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = ListNode()
        cur = merged_list


        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        
        if list1 is None:
            cur.next = list2
        else:
            cur.next = list1
        
        return merged_list.next
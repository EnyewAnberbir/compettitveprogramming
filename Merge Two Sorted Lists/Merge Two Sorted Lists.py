class Solution(object):
    def mergeTwoLists(self, list1, list2):
        last = ListNode(-1)

        current = last
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next            
            current = current.next

        if list1 is not None:
            current.next = list1
        else:
            current.next = list2

        return last.next

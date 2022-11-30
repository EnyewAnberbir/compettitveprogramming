# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        var = head
        while head and head.next:
            head.val, head.next.val = head.next.val, head.val
            head = head.next.next
        return var

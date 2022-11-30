# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        low = head
        high = head

        while high and high.next:
            low = low.next
            high = high.next.next

        return low

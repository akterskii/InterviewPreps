# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        head2 = None
        tmp1 = None
        while head is not None:
            tmp = head.next
            head.next = head2
            head2 = head
            head = tmp
        return head2
            
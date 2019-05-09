# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = None
        cur_min=[]
        empty = 0
        for i,el in enumerate(lists):
            if el is not None:
                cur_min.append([el.val,i])
            else:
                empty += 1
        heapq.heapify(cur_min)
        
        head = ListNode(-1)
        p = head
        while empty<len(lists):
            cur_val, num = heapq.heappop(cur_min)
            
            p.next = lists[num]
            p = p.next
            lists[num]=lists[num].next
            if lists[num] is not None:
                heapq.heappush(cur_min,[lists[num].val,num])
            else:
                empty+=1
            p.next = None
        return head.next
            
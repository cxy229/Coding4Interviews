# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        prek = head
        cur = head
        for i in range(k):
            if cur is None:
                return None
            cur = cur.next
        while cur:
            prek = prek.next
            cur = cur.next
        return prek

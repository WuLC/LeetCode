# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-06-27 21:04:01
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-27 21:04:11
# @Email: liangchaowu5@gmail.com

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        p1, p2 = dummy, head
        while p2:
            if p2.val == val:
                while p2 and p2.val == val:
                    p2 = p2.next
                p1.next = p2
                p1 = p1.next
                if p1:
                    p2 = p1.next
                else:
                    break
            else:
                p1, p2 = p2, p2.next
        return dummy.next
                
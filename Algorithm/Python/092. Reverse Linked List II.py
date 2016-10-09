# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-05-30 16:48:17
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-30 16:48:27
# @Email: liangchaowu5@gmail.com

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        p, count = dummy, 1
        while p.next != None:
            if count == m:
                start = p
                p1 = p.next
                p2 = p1.next
                while True:
                    if count == n:
                        start.next.next = p2
                        start.next = p1
                        return dummy.next
                    tmp = p2.next
                    p2.next = p1
                    p1 = p2 
                    p2 = tmp
                    count += 1     
            p = p.next
            count += 1
        return dummy.next # only one ListNode
        
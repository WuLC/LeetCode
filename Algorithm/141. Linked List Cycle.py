# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-06-15 21:31:56
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-15 21:32:38
# @Email: liangchaowu5@gmail.com


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None: return False
        tmp, p = head, head.next
        while p:
            if tmp == tmp.next: return True
            tmp.next = tmp
            tmp = p
            p = p.next
        return False
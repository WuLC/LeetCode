# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-06-15 21:31:56
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-15 21:40:13
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
        while head:
            if head == head.next: return True
            p = head.next 
            head.next = head
            head = p
        return False
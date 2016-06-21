# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-06-21 16:03:27
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-21 16:03:37
# @Email: liangchaowu5@gmail.com

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        p1, p2 = head, head.next
        p1.next = None
        while p2:
            p3 = p2.next
            p2.next = p1 
            p1, p2 = p2, p3
        return p1
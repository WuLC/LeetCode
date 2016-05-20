# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-20 08:29:29
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-20 09:49:58
# @Email: liangchaowu5@gmail.com

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# two pointers
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        p1 = head
        p2 = head.next
        while p2:
            if p2.val != p1.val:
                p1.next = p2
                p1 = p2
            p2 = p2.next
        p1.next = None
        return head
            
        
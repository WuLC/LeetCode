# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-06-15 21:31:56
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-28 14:28:20
# @Email: liangchaowu5@gmail.com


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# method 1, modify the link list
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

# method 2, tow pointers
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p1 = p2 = head
        while p1 and p2:
            if p1.next:
                p1 = p1.next.next
            else:
                return False
            p2 = p2.next
            if p1 == p2:
                return True
        return False
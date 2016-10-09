# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-06-23 16:17:53
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-23 16:19:52
# @Email: liangchaowu5@gmail.com

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        p1, p2 = headA, headB
        r1, r2 = False, False
        while True:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next
            if p1 == None:
                if r1:
                    return None
                else:
                    r1 = True
                    p1 = headB
            if p2 == None:
                if r2:
                    return None
                else:
                    r2 = True
                    p2 = headA        
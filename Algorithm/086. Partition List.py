# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-05-26 17:53:02
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-26 17:53:15
# @Email: liangchaowu5@gmail.com

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        p1, ip = dummy, None
        start, end = None, None
        while ip == None and p1.next!=None:
            if p1.next.val >= x :
                ip = p1
            p1 = p1.next
            
        while p1.next != None:
            if p1.next.val < x:
                if start == None:
                    start = end = p1.next
                else:
                    end.next = p1.next
                    end = end.next
                p1.next = p1.next.next
            else:
                p1 = p1.next
            
        if ip!= None and start != None:
            end.next = ip.next
            ip.next = start
        return dummy.next
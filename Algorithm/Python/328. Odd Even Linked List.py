# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-06-19 14:08:01
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-19 14:08:17
# @Email: liangchaowu5@gmail.com

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count, odd, even, t1, t2= 1, None, None, None, None
        while head:
            if count % 2 == 1:
                if odd == None: 
                    odd = head
                    t1 = head
                else:
                    t1.next = head
                    t1 = head
            else:
                if even == None: 
                    even = head
                    t2 = head
                else:
                    t2.next = head
                    t2 = head
            head = head.next
            count += 1
        if t1 != None:
            t1.next = even
        if t2 != None:
            t2.next = None
        return odd
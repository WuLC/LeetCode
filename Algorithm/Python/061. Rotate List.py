# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-05-10 10:41:22
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-10 10:47:29
# @Email: liangchaowu5@gmail.com

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Two pointers
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        p1,p2 = dummy,dummy
        # when k> length of list,k = k%n
        tmp = dummy
        n=0
        while tmp.next!=None:
            tmp = tmp.next
            n+=1
        if n==0:
            return dummy.next
        k %= n
        for i in xrange(k):
            p2 = p2.next
        while p2.next != None:
            p1 = p1.next
            p2 = p2.next
        if p1.next == head or p1.next==None:  # when k==0 or k==the length of list
            return dummy.next
        else:
            dummy.next = p1.next
            p2.next = head
            p1.next = None
            return dummy.next
            
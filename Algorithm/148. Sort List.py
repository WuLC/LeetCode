# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-05 17:16:47
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-05 17:16:58
# @Email: liangchaowu5@gmail.com

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr, length = head, 0
        while curr:
            length += 1
            curr = curr.next
        dummy, dummy.next = ListNode(0), head
        step =  1
        while step < length:
            curr, tail = dummy.next, dummy
            while curr:
                left = curr
                right = self.split(curr, step)
                curr = self.split(right, step)
                h, t = self.merge(left, right)
                tail.next = h
                tail = t
            step <<= 1
        return dummy.next
            
            
    
    def split(self, head,n):
        while head and n>0:
            if n == 1:
                tmp = head.next
                head.next = None
                return tmp
            head = head.next
            n -= 1
        return None
            
    
    # return head and tail of two merged list
    def merge(self, head1, head2):
        dummy = ListNode(0)
        curr = dummy
        while head1 and head2:
            if head1.val > head2.val:
                curr.next = head2
                head2 = head2.next
            else:
                curr.next = head1
                head1 = head1.next
            curr = curr.next
        if head1:
            curr.next = head1
        if head2:
            curr.next = head2
        while curr.next:
            curr = curr.next
        return dummy.next, curr